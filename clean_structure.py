"""
تنظيف وإعادة بناء هيكل CodeForge
"""

import os
import shutil
from pathlib import Path

def clean_project():
    """تنظيف المشروع"""
    print("🧹 تنظيف CodeForge...")
    
    # الملفات/المجلدات للحذف
    to_delete = [
        # ملفات مؤقتة
        "setup.py", "test_*.py", "run*.py", "simple_*.py", "fixed_*.py",
        
        # مشاريع تجريبية
        "my_*", "test_*",
        
        # مجلدات __pycache__
        "__pycache__",
        
        # ملفات .egg-info إذا وجدت
        "*.egg-info", "build", "dist"
    ]
    
    for pattern in to_delete:
        for item in Path(".").glob(pattern):
            if item.is_dir():
                shutil.rmtree(item, ignore_errors=True)
                print(f"  🗑️  حذف مجلد: {item}")
            else:
                item.unlink(missing_ok=True)
                print(f"  🗑️  حذف ملف: {item}")
    
    print("✅ تم التنظيف!")

def verify_structure():
    """التحقق من الهيكل"""
    print("\n🔍 التحقق من الهيكل...")
    
    required = {
        "src/codeforge/__init__.py": True,
        "src/codeforge/core/version.py": True,
        "src/codeforge/modules/scaffolder/engine.py": True,
        "src/codeforge/templates/python_basic/README.md.j2": True,
        "pyproject.toml": True,
        "cli_main.py": True,
    }
    
    all_ok = True
    for path, required in required.items():
        if Path(path).exists():
            print(f"  ✅ {path}")
        else:
            print(f"  ❌ {path} (مفقود)")
            all_ok = False
    
    return all_ok

def create_missing():
    """إنشاء الملفات المفقودة"""
    print("\n🔨 إنشاء الملفات المفقودة...")
    
    # __init__.py files
    init_files = [
        "src/codeforge/__init__.py",
        "src/codeforge/core/__init__.py",
        "src/codeforge/modules/__init__.py",
        "src/codeforge/modules/scaffolder/__init__.py",
    ]
    
    for file in init_files:
        if not Path(file).exists():
            Path(file).parent.mkdir(parents=True, exist_ok=True)
            Path(file).touch()
            print(f"  📄 أنشئ: {file}")

def main():
    """الدالة الرئيسية"""
    print("=" * 50)
    print("🛠️  إعادة بناء هيكل CodeForge")
    print("=" * 50)
    
    clean_project()
    
    if verify_structure():
        print("\n🎉 الهيكل صحيح!")
        print("\n📁 الهيكل الحالي:")
        os.system("dir /B src\\codeforge")
    else:
        create_missing()
        print("\n⚠️  تم إنشاء بعض الملفات، تحقق يدوياً")

if __name__ == "__main__":
    main()