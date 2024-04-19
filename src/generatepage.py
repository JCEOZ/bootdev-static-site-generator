

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.strip().startswith('# '):
            # Grab the header text
            return line.strip()[2:]
    raise Exception('Could not find title in markdown')