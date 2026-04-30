from flask import Flask, render_template, jsonify
import os

# إعداد التطبيق - تم تحديد template_folder بنفس المجلد لتسهيل الرفع
app = Flask(__name__, template_folder='.')

# المحطة الرئيسية: عرض واجهة المستخدم
@app.route('/')
def index():
    return render_template('index.html')

# API: خدمات تيليجرام
@app.route('/api/services/telegram')
def telegram_services():
    return jsonify({
        "status": "success",
        "category": "خدمات تيليجرام الاحترافية"
    })

# API: الذكاء الاصطناعي
@app.route('/api/services/ai')
def ai_services():
    return jsonify({
        "status": "success",
        "category": "الذكاء الاصطناعي والتصميم"
    })

if __name__ == '__main__':
    # التشغيل على المنفذ 3000 أو المنفذ الذي يحدده السيرفر
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)