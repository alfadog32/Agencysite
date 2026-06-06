import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure session key for flash messages

# Mock Database for available protection tiers
TIERS = {
    "essential": {"name": "Essential Shield", "price": "$149/mo", "scans": "Daily Scans", "platforms": "Top 10 Leak Sites"},
    "elite": {"name": "Elite Monitor", "price": "$299/mo", "scans": "Real-time Monitoring", "platforms": "Global Web + Telegram"},
    "enterprise": {"name": "VIP Total Control", "price": "$599/mo", "scans": "Continuous Scanning", "platforms": "Full Web, Torrent, + Legal DMCA"}
}

@app.route('/')
def index():
    """Renders the high-end, premium landing page selling the service."""
    return render_template('index.html', tiers=TIERS)

@app.route('/checkout/<tier_id>', methods=['GET', 'POST'])
def checkout(tier_id):
    """Handles upfront payment onboarding selection."""
    tier = TIERS.get(tier_id)
    if not tier:
        flash("Invalid plan selected.", "error")
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        # Capture model onboarding details
        model_name = request.form.get('model_name')
        of_username = request.form.get('of_username')
        email = request.form.get('email')
        
        # Integration Point: This is where you pass data to Stripe/Crypto API
        # print(f"Processing upfront payment for {model_name} ({email}) - Tier: {tier['name']}")
        
        flash(f"Account created successfully for {model_name}! Redirecting to secure billing module...", "success")
        return redirect(url_for('dashboard'))
        
    return render_template('checkout.html', tier=tier)

@app.route('/dashboard')
def dashboard():
    """Secure client portal showing leak scanning metrics once paid."""
    # Mock data to simulate the system working after they subscribe
    mock_metrics = {
        "scans_completed": 142,
        "leaks_detected": 18,
        "takedowns_issued": 12,
        "status": "Active Shielding"
    }
    return render_template('dashboard.html', metrics=mock_metrics)

if __name__ == '__main__':
    # Running locally on your Windows 11 machine
    app.run(debug=True, port=5000)