# 📱 HackerLocker — دليل وملفات بناء تطبيق أندرويد (APK)

هذا المجلد يحتوي على كامل الملفات اللازمة لتحويل التطبيق إلى ملف تثبيت أندرويد حقيقي بصيغة **`.apk`** يعمل على أجهزة أندرويد عبر **Buildozer + python-for-android**.

| الملف | الوظيفة |
|---|---|
| [main.py](file:///c:/Users/RameAlysfy/Desktop/HackerLocker/apk_build/main.py) | نقطة انطلاق التطبيق المبنية بمكتبة Kivy (كلمة المرور الافتراضية: `782106202`) |
| [logo.png](file:///c:/Users/RameAlysfy/Desktop/HackerLocker/apk_build/logo.png) | شعار التطبيق — يُستخدم كأيقونة للتطبيق وشاشة بدء (Splash Screen) |
| [buildozer.spec](file:///c:/Users/RameAlysfy/Desktop/HackerLocker/apk_build/buildozer.spec) | ملف تكوين وإعدادات البناء (معمارية `arm64-v8a` المعتمدة لجميع الأجهزة الحديثة) |
| [Colab_Build_APK.ipynb](file:///c:/Users/RameAlysfy/Desktop/HackerLocker/apk_build/Colab_Build_APK.ipynb) | مفكرة Google Colab جاهزة للبناء السحابي المجاني بضغطة زر وتنزيل الـ APK مباشرة |
| [.github/workflows/build-apk.yml](file:///c:/Users/RameAlysfy/Desktop/HackerLocker/.github/workflows/build-apk.yml) | ملف سير العمل للبناء التلقائي عبر GitHub Actions |

---

## 🌟 الطريقة 1 — عبر GitHub Actions (تلقائي وسحابي مجاناً)

1. ارفع المشروع إلى مستودع على **GitHub**.
2. افتح تبويب **Actions** في مستودعك.
3. اختر سير العمل **Build HackerLocker APK** واضغط **Run workflow**.
4. انتظر انتهاء البناء (يستغرق البناء من 20 إلى 35 دقيقة تقريباً).
5. ادخل على صفحة نتيجة التشغيل، وستجد ملف الـ APK جاهزاً للتحميل داخل قسم **Artifacts** باسم `HackerLocker-Android-APK`.

---

## 🚀 الطريقة 2 — عبر Google Colab (بدون حاجة لـ GitHub)

1. افتح [Google Colab](https://colab.research.google.com).
2. ارفع ملف [Colab_Build_APK.ipynb](file:///c:/Users/RameAlysfy/Desktop/HackerLocker/apk_build/Colab_Build_APK.ipynb) إليه.
3. ارفع الملفات الثلاثة (`main.py` و `buildozer.spec` و `logo.png`).
4. اضغط **Runtime -> Run all**.
5. بمجرد انتهاء البناء سيتم تنزيل ملف الـ APK إلى جهازك تلقائياً.

---

## 💻 الطريقة 3 — البناء محلياً على حاسوبك (WSL أو Linux)

```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

pip install --upgrade cython buildozer
cd apk_build
buildozer -v android debug
```

الملف الناتج يظهر في مجلد `apk_build/bin/` باسم:
`HackerLocker-1.0.0-arm64-v8a-debug.apk`