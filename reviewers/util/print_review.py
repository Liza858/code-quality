from reviewers.review_result import ReviewResult


def print_review(review: ReviewResult):
    if not review.issues:
        print(f'ok')
        return

    issues_by_category = {}
    for issue in review.issues:
        issues_by_category.setdefault(issue.category, []).append(issue)

    number = 1
    for category in issues_by_category:
        issues = issues_by_category[category]
        print(f'\ncategory: {category}\n')
        for issue in issues:
            print(f'{number})')
            print(f'  category: {issue.category}')
            print(f'  text: {issue.text}')
            print(f'  file: {issue.file}')
            print(f'  line number: {issue.line_number}')
            print(f'  column number: {issue.column_number}')
            print("*************************************************")
            number += 1
