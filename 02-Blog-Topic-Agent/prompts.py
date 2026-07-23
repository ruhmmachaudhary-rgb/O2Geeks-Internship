def topic_prompt(company_name):

    return f"""
You are an expert AI Content Strategist.

Generate 5 trending blog topics for the following AI software company.

Company Name:
{company_name}

Requirements:
- Generate exactly 5 topics.
- Topics should be unique.
- Topics should be trending in AI.
- Topics should be SEO-friendly.
- Topics should attract business clients.
- Return only a numbered list.
"""


def blog_prompt(topic):

    return f"""
You are an expert SEO Blog Writer.

Write a professional, engaging and SEO-friendly blog on the following topic.

Topic:
{topic}

Follow this structure exactly:

# Title

## Meta Description
(Write 2-3 lines)

## Focus Keywords
(List 5 keywords)

## Introduction

## Heading 1

## Heading 2

## Heading 3

## Conclusion

## Call to Action

Requirements:
- Write between 700 and 1000 words.
- Use professional English.
- Use headings and subheadings.
- Use bullet points where appropriate.
- Make the content informative and original.
- Do not use emojis.
- Return only the blog.
"""


def extract_topics_prompt(company_name):

    return f"""
Generate exactly 5 trending blog topics for the following company.

Company:
{company_name}

Rules:
- Return only topic names.
- One topic per line.
- No numbering.
- No explanation.
"""
def company_analysis_prompt(company):

    return f"""
You are a business analyst.

Analyze the software company below.

Company:
{company}

Return the information in this format:

Company Name:
Industry:
Services:
Products:
Target Audience:
Technologies Used:
Short Summary:

Keep the response professional and under 200 words.
"""