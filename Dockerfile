FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl tesseract-ocr && rm -rf /var/lib/apt/lists/*

# انزل uv installing
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# uv path
ENV PATH="/root/.local/bin:$PATH"

# download libraries 
COPY pyproject.toml uv.lock ./

# لو عندي جاهز بخليه ياخد من toml
RUN uv sync --frozen

COPY . .

# port
EXPOSE 8501

CMD ["uv","run","streamlit", "run", "app/streamlitApp.py", "--server.port=8501", "--server.address=0.0.0.0"]

# uv run streamlit run app/streamlitApp.py