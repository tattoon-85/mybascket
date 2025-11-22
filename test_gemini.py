import google.generativeai as genai

# ---------------------------------------------------------
# ここに直接キーを書いてください
# " " の中身を、AIza から始まる長い文字列に書き換えてください
# ---------------------------------------------------------
my_api_key = "AIzaSyAhX7kLqgGHl9AcUmyZTlOnbXoDki4tztk"  # ←ここに、取得したAPIキーを貼り付ける！

genai.configure(api_key=my_api_key)

print("--- あなたのAPIキーで利用可能なモデル一覧 ---")
try:
    available_models = []
    # モデル一覧を取得
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
            available_models.append(m.name)
    
    print("---------------------------------------------")

    # 一覧の最初のモデルを使ってテスト
    if available_models:
        target_model = available_models[0] # 自動で最初のやつを選ぶ
        print(f"\nモデル '{target_model}' で生成を試みます...")
        
        model = genai.GenerativeModel(target_model)
        response = model.generate_content("龍生です。一言挨拶して！")
        
        print("\nResponse:")
        print(response.text)
    else:
        print("利用可能なモデルが見つかりませんでした。")

except Exception as e:
    print(f"\nエラーが発生しました:\n{e}")