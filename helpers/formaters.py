def offer_formater(offer: dict) -> str:
    lines = []
    for key, value in offer.items():
        lines.append(f"{key}: {value}")
    return "\n".join(lines)


def format_post(post: dict) -> str:
    lines = []

    title = post.get("title", "")
    if title:
        lines.append(f"{title}\n")

    for key, value in post.items():
        if key in ["title", "id"]:
            continue
        if value:

            value_str = str(value)
            lines.append(f"*{key}*: {value_str}")

    return "\n".join(lines)