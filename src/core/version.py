"""
إدارة إصدارات CodeForge
"""

from typing import Tuple

# الإصدار الحالي
VERSION = (0, 1, 0)  # (MAJOR, MINOR, PATCH)

def get_version() -> str:
    """الحصول على الإصدار كـ string"""
    return ".".join(map(str, VERSION))

def get_version_tuple() -> Tuple[int, int, int]:
    """الحصول على الإصدار كـ tuple"""
    return VERSION

def print_version() -> None:
    """طباعة الإصدار بشكل جميل"""
    try:
        from colorama import Fore, Style, init
        init(autoreset=True)
        
        version_str = get_version()
        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}🚀 CodeForge v{version_str}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}📦 منشئ المشاريع البرمجية{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    except ImportError:
        # إذا colorama غير مثبت
        print(f"CodeForge v{get_version()}")