def build_explanaiton_prompt(anomalies: list[dict]) -> str:
    lines = ["Explain the following data quality issues:\n"]
    
    for a in anomalies:
        line = f"- Column '{a.get('column')}' has issue '{a.get('type')}'."
        lines.append(line)

    return "\n".join(lines)