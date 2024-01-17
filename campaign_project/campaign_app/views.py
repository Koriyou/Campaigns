# Campaign_Manager/campaign_app/views.py


def index(request):
    return render(request, 'campaign_app/index.html')

import os
import markdown
from django.conf import settings
from django.shortcuts import render


def campaign1(request):
    # Construct the path to the campaigns_markdown directory
    markdown_directory = os.path.join(settings.BASE_DIR, 'campaigns_markdown')

    # Initialize a list to store session content
    session_content = []

    # Iterate through session files in the campaign directory
    for filename in os.listdir(markdown_directory):
        if filename.endswith(".md"):
            # Read the Markdown content from the file
            with open(os.path.join(markdown_directory, filename), "r", encoding="utf-8") as file:
                markdown_content = file.read()

                # Convert Markdown to HTML
                html_content = markdown.markdown(markdown_content)

                # Add the HTML content to the list
                session_content.append(html_content)

    # Pass the markdown content to the template
    context = {"markdown_content": session_content}
    return render(request, "campaign_app/Campaign1.html", context)




# Define more views as needed
