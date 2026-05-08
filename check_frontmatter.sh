#!/bin/bash
# Frontmatter Quality Checker for Paper Library
# Checks all markdown files in Outputs against CLAUDE.md standards

OUTPUTS="/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Outputs"
REQUIRED_FIELDS=("title" "authors" "date" "year" "journal" "abstract" "abstract_cn" "cite" "aiSum" "keywords")

echo "========================================="
echo "FRONTMATTER QUALITY AUDIT REPORT"
echo "========================================="
echo ""

TOTAL=0
PASS=0
SINGLE_QUOTE_FILES=()
MISSING_FIELDS_FILE="/tmp/missing_fields.txt"
> "$MISSING_FIELDS_FILE"

while IFS= read -r -d '' file; do
    # Skip non-paper .md files (like .claude/ agents)
    if [[ "$file" == *".claude/"* ]]; then
        continue
    fi

    TOTAL=$((TOTAL + 1))
    filename=$(basename "$file")

    # Extract frontmatter (between --- and ---)
    frontmatter=$(sed -n '/^---$/,/^---$/p' "$file" | sed '1d;$d')

    if [ -z "$frontmatter" ]; then
        echo "  MISSING-FM | $filename"
        continue
    fi

    issues=""

    # Check 1: Single quotes in frontmatter (should use double quotes)
    single_quotes=$(echo "$frontmatter" | grep -n "'" | grep -v "^[0-9]*:[[:space:]]*#" | grep -v "''" || true)
    if [ -n "$single_quotes" ]; then
        issues="${issues} [SINGLE-QUOTES]"
    fi

    # Check 2: Required fields
    for field in "${REQUIRED_FIELDS[@]}"; do
        if ! echo "$frontmatter" | grep -q "^${field}:"; then
            issues="${issues} [MISSING:${field}]"
            echo "$file|MISSING:${field}" >> "$MISSING_FIELDS_FILE"
        fi
    done

    # Check 3: Keywords format - should contain [[
    keywords_line=$(echo "$frontmatter" | grep "^keywords:" || true)
    if [ -n "$keywords_line" ]; then
        # Check if keywords use wikilinks [[ ]]
        has_wikilinks=$(echo "$frontmatter" | grep -A50 "^keywords:" | grep "\[\[" || true)
        if [ -z "$has_wikilinks" ]; then
            issues="${issues} [NO-WIKILINKS]"
        fi
    fi

    # Check 4: authors should be a list (start with - on next line)
    authors_line=$(echo "$frontmatter" | grep -A1 "^authors:" | tail -1)
    if ! echo "$authors_line" | grep -q "^\s*-\s"; then
        issues="${issues} [AUTHORS-NOT-LIST]"
    fi

    if [ -z "$issues" ]; then
        PASS=$((PASS + 1))
    else
        echo "  FAIL | $(dirname "$(dirname "$file")")/$(basename "$file")"
        echo "         $issues"
    fi

done < <(find "$OUTPUTS" -name "*.md" -type f -print0)

echo ""
echo "========================================="
echo "SUMMARY"
echo "========================================="
echo "  Total papers checked: $TOTAL"
echo "  Passed: $PASS"
echo "  Failed: $((TOTAL - PASS))"
echo ""

# Show missing fields summary
if [ -s "$MISSING_FIELDS_FILE" ]; then
    echo "--- Missing Fields Breakdown ---"
    cat "$MISSING_FIELDS_FILE" | awk -F'|' '{print $2}' | sort | uniq -c | sort -rn
fi
