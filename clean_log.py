import json
import os
import re

def clean_log(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        return f"Error reading file: {e}"

    extracted_text = []
    
    # Navigate to the chunks
    # Based on the file structure seen: root -> chunkedPrompt -> chunks
    chunks = data.get('chunkedPrompt', {}).get('chunks', [])
    
    if not chunks:
        return "No chunks found in the file. Is this a valid Google AI Studio export?"

    for chunk in chunks:
        role = chunk.get('role', 'unknown')
        
    current_role = None
    current_message_buffer = []

    for chunk in chunks:
        role = chunk.get('role', 'unknown').upper()
        chunk_text = ""
        
        # Prioritize 'parts' if available
        if 'parts' in chunk and chunk['parts']:
            for part in chunk['parts']:
                # Skip thoughts entirely based on user request
                if part.get('thought', False):
                    continue
                if 'text' in part:
                    chunk_text += part['text']
        # Fallback to 'text' if no parts
        elif 'text' in chunk:
            chunk_text = chunk['text']
            
        # If we have text, handle merging
        if chunk_text:
            # If role changed, flush the previous buffer
            if role != current_role:
                if current_role is not None and current_message_buffer:
                    full_message = "".join(current_message_buffer).strip()
                    if full_message:
                        # Remove Markdown characters (* and #)
                        full_message = re.sub(r'[*#]', '', full_message)
                        extracted_text.append(f"**{current_role}**: {full_message}\n\n")
                
                # Start new buffer for new role
                current_role = role
                current_message_buffer = [chunk_text]
            else:
                # Same role, append to buffer
                current_message_buffer.append(chunk_text)
    
    # Flush the final buffer
    if current_role is not None and current_message_buffer:
        full_message = "".join(current_message_buffer).strip()
        if full_message:
            # Remove Markdown characters (* and #)
            full_message = re.sub(r'[*#]', '', full_message)
            extracted_text.append(f"**{current_role}**: {full_message}\n\n")
    
    # Join all text
    full_text = "\n".join(extracted_text)
    
    # Calculate stats
    original_size = os.path.getsize(file_path)
    new_size = len(full_text.encode('utf-8'))
    
    # Save to a new file
    output_path = file_path + "_cleaned.txt"
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_text)
    except Exception as e:
        return f"Error saving file: {e}"

    # Prepare result message
    reduction = ((original_size - new_size) / original_size) * 100
    result_msg = (
        f"Success!\n"
        f"Original Size: {original_size} bytes\n"
        f"Cleaned Size:  {new_size} bytes\n"
        f"Reduction:     {reduction:.2f}%\n"
        f"Saved to:      {output_path}"
    )
    return result_msg

if __name__ == "__main__":
    # The file name provided by the user
    target_file = r"d:\class\projects\Log2Text\漫画：无限与不可逆。"
    print(clean_log(target_file))
