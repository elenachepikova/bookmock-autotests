FROM python:3.12-slim

WORKDIR /app

COPY . .

    # Utilities for downloading, unzipping and adding repository keys
RUN apt-get update && apt-get install -y wget unzip gnupg \
    # Download Google public key
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    # Add Google Chrome repository to package sources
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    # Install Chrome stable version
    && apt-get update && apt-get install -y google-chrome-stable \
    # ChromeDriver download
    && wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/$(google-chrome-stable --version | cut -d ' ' -f 3)/linux64/chromedriver-linux64.zip \
    # Unzip ChromeDriver
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    # Rights to use ChromeDriver
    && chmod +x /usr/local/bin/chromedriver-linux64 \
    # Make useful link
    && ln -s /usr/local/bin/chromedriver-linux64 /usr/local/bin/chromedriver \
    # Install python dependencies
    && pip install --no-cache-dir -r requirements.txt \
    # Clear cash
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV HEADLESS=true

CMD ["python", "-m", "pytest"]