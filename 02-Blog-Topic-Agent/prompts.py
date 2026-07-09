def topic_prompt(company_name):

    return f"""
You are an expert AI Content Strategist.

Your task is to generate 5 trending weekly blog topics for an AI services provider software company.

Company Name:
{company_name}

Rules:
- Generate exactly 5 topics.
- Topics should be unique.
- Topics should be SEO-friendly.
- Topics should be relevant to AI and software services.
- Return only the numbered list.
"""
def blog_prompt(topic):

    return f"""
You are an expert technical blog writer.

Write a professional blog on this topic.

Topic:
{topic}

Include:
- Title
- Introduction
- 3 Headings
- Conclusion
"""
def extract_topics_prompt(company_name):

    return f"""
Generate exactly 5 trending weekly blog topics for {company_name}.

Rules:
- Return only the topic names.
- One topic per line.
- No numbering.
- No explanation.
"""