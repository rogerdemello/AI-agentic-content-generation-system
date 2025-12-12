"""
Vercel serverless function for content generation
"""
import json
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from orchestrator import WorkflowOrchestrator
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    """Vercel serverless handler for content generation API"""
    
    def do_GET(self):
        """Serve a simple frontend for local testing or respond to favicon requests"""
        # Serve the public/index.html on root requests to make local testing easier
        if self.path in ('/', '/index.html'):
            try:
                index_path = os.path.join(os.path.dirname(__file__), '..', 'public', 'index.html')
                with open(index_path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(content)
            except Exception:
                self.send_response(500)
                self.end_headers()
        elif self.path == '/favicon.ico':
            self.send_response(204)
            self.end_headers()
        else:
            # For other GET paths, return 404
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        """Handle POST request with product data"""
        try:
            # Parse request body
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))
            
            # Extract product data
            product_a_data = data.get('product_a')
            product_b_data = data.get('product_b')
            
            if not product_a_data:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                error = {'error': 'product_a is required'}
                self.wfile.write(json.dumps(error).encode())
                return
            
            # Initialize orchestrator
            orchestrator = WorkflowOrchestrator()
            
            # Execute pipeline
            results = orchestrator.execute_pipeline_from_data(
                product_a_data=product_a_data,
                product_b_data=product_b_data
            )
            
            # Return generated content
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                'success': True,
                'outputs': results['outputs'],
                'agents_executed': results['agents_executed']
            }
            
            self.wfile.write(json.dumps(response, indent=2).encode())
            
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            error = {'error': 'Invalid JSON'}
            self.wfile.write(json.dumps(error).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            error = {'error': str(e)}
            self.wfile.write(json.dumps(error).encode())
    
    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
