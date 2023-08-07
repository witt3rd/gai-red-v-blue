import json
import os
import re

response = """
{
    "action": "Final Answer",
    "action_input": "To organize this business dinner, we'll go through several steps:
1. **Identify Potential Attendees:** Based on our client list, we'll identify organizations which have expressed interest in artificial intelligence or are in industries where AI adoption is trending. We'll then identify technical executives in those organizations.
2. **Prequalification:** We'll reach out to these executives with a brief survey or a set of questions to gauge their interest in generative AI and their readiness to adopt such technologies. This will help us ensure that the dinner is filled with executives who are genuinely interested and have the potential to implement AI in their businesses.
3. **Venue Selection:** We'll look for a high-end venue that offers a private dining area with multimedia capabilities for our presentation/demonstration. The venue should offer a quiet and sophisticated atmosphere suitable for executives.
4. **Presentation Planning:** We'll prepare a compelling presentation/demonstration showcasing how generative AI can be beneficial for their businesses. We'll focus on real-world examples, potential ROI, and implementation strategies.
5. **Invitations:** Once we've narrowed down our list to ~12 executives and secured a venue, we'll send out formal invitations for the dinner. The invitations will outline the purpose of the dinner, the topics to be discussed, and will include a request for any specific questions or topics they'd like us to cover.
6. **Follow-ups:** Post dinner, we'll follow up with each executive, thanking them for their time and providing additional resources or setting up further meetings as needed."
}
"""
response = json.loads(response, strict=False)
response = response["action_input"]
print(response)
