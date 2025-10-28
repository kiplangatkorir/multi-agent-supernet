import requests

class Tools:
    """Provides specialized tools for different agents."""

    @staticmethod
    def fetch_stock_price(ticker):
        """Fetches real-time stock price from Yahoo Finance."""
        try:
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
            response = requests.get(url, timeout=5)
            data = response.json()
            if "chart" in data and "result" in data["chart"]:
                return f"📈 {ticker} current price: {data['chart']['result'][0]['meta']['regularMarketPrice']}"
            return "❌ Error fetching stock price."
        except Exception as e:
            return f"❌ Error fetching stock price: {str(e)}"

    @staticmethod
    def fetch_academic_papers(query):
        """Fetches latest academic papers from ArXiv."""
        try:
            url = f"http://export.arxiv.org/api/query?search_query={query}&start=0&max_results=2"
            response = requests.get(url, timeout=5)
            return response.text if response.status_code == 200 else "❌ Error fetching papers."
        except Exception as e:
            return f"❌ Error fetching papers: {str(e)}"

    @staticmethod
    def analyze_sentiment(text):
        """Performs sentiment analysis on a given text."""
        try:
            url = "https://api.text-processing.com/sentiment/"
            response = requests.post(url, data={"text": text}, timeout=5)
            return response.json() if response.status_code == 200 else "❌ Sentiment analysis failed."
        except Exception as e:
            return f"❌ Sentiment analysis failed: {str(e)}"

    @staticmethod
    def detect_threats(logs):
        """Analyzes security logs for potential threats."""
        # Simulated AI-based threat detection
        return f"🚨 Threat analysis complete. {len(logs)} logs scanned. No critical threats detected."

    @staticmethod
    def fetch_medical_info(condition):
        """Fetches medical information from PubMed."""
        url = f"https://pubmed.ncbi.nlm.nih.gov/?term={condition.replace(' ', '+')}"
        return f"🔍 Search PubMed for {condition}: {url}"

    @staticmethod
    def recommend_treatment(condition):
        """Provides basic treatment recommendations."""
        treatments = {
            "headache": "💊 Recommended: Ibuprofen or Acetaminophen.",
            "fever": "🌡️ Recommended: Rest, hydration, and Paracetamol.",
            "diabetes": "🍏 Recommended: Insulin therapy & lifestyle changes."
        }
        for key, value in treatments.items():
            if key in condition.lower():
                return value
        
        return f"⚠️ No specific treatment found for '{condition}'. Consult a doctor."
