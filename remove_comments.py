import os
import re

def remove_java_comments(text):
    text = re.sub(r'//.*', '', text)
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    return text

def remove_xml_comments(text):
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    return text

def remove_jsp_comments(text):
    text = re.sub(r'<%--.*?--%>', '', text, flags=re.DOTALL)
    text = remove_xml_comments(text)
    return text

project_dir = r'D:\Study\NAM3\KY1\DOT1\WEB\Workspace\Web_ktgk\src'
for root, dirs, files in os.walk(project_dir):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        if file.endswith('.java'):
            new_content = remove_java_comments(content)
        elif file.endswith('.xml'):
            new_content = remove_xml_comments(content)
        elif file.endswith('.jsp'):
            new_content = remove_jsp_comments(content)
            
        if new_content != content:
            # Clean up extra blank lines
            new_content = re.sub(r'\n\s*\n', '\n\n', new_content)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

# Handle pom.xml
pom_path = r'D:\Study\NAM3\KY1\DOT1\WEB\Workspace\Web_ktgk\pom.xml'
if os.path.exists(pom_path):
    with open(pom_path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = remove_xml_comments(content)
    new_content = re.sub(r'\n\s*\n', '\n\n', new_content)
    with open(pom_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Comments removed.")
