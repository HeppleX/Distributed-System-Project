from app import create_app

# 启动 Flask 应用
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
