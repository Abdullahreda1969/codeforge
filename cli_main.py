"""
واجهة CLI لـ CodeForge مع هوية بصرية كاملة
"""

import sys
import os
from pathlib import Path

# أضف src إلى المسار
current_dir = Path(__file__).parent
src_path = current_dir / "src"
sys.path.insert(0, str(src_path))

import click
from colorama import init, Fore, Style, Back

# تهيئة colorama
init(autoreset=True)
def print_colored_logo():
    """طباعة شعار CodeForge ملون"""
    from colorama import Fore, Style, Back
    
    logo = f"""
{Style.BRIGHT}{Fore.BLUE}
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║  {Fore.CYAN}   _____          ______                          {Fore.BLUE}  ║
    ║  {Fore.CYAN}  / ____|        |  ____|                         {Fore.BLUE}  ║
    ║  {Fore.CYAN} | |     ___   __| |__ _ __ ___  ___              {Fore.BLUE}  ║
    ║  {Fore.CYAN} | |    / _ \\ / _`  __| '__/ _ \\/ _ \\             {Fore.BLUE}  ║
    ║  {Fore.CYAN} | |___| (_) | (_| |  | | |  __/  __/             {Fore.BLUE}  ║
    ║  {Fore.CYAN}  \\_____\\___/ \\__,_|  |_|  \\___|\\___|             {Fore.BLUE}  ║
    ║                                                          ║
    ║        {Fore.YELLOW}🔨 {Style.BRIGHT}The Code Forge{Style.NORMAL}                     {Fore.BLUE}  ║
    ║        {Fore.WHITE}From Idea to Deployment{Style.NORMAL}                 {Fore.BLUE}  ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}

{Fore.YELLOW}┌────────────────────────────────────────────────────────────┐{Style.RESET_ALL}
{Fore.YELLOW}│{Style.RESET_ALL}    {Style.BRIGHT}🚀 CodeForge CLI v0.1.0 - Forge Your Code Efficiently{Style.RESET_ALL}    {Fore.YELLOW}│{Style.RESET_ALL}
{Fore.YELLOW}│{Style.RESET_ALL}    {Fore.CYAN}https://github.com/Abdullahreda1969/codeforge{Style.RESET_ALL}         {Fore.YELLOW}│{Style.RESET_ALL}
{Fore.YELLOW}└────────────────────────────────────────────────────────────┘{Style.RESET_ALL}
    """
    print(logo)

# ثم في دالة cli الرئيسية:
@click.group()
def cli():
    """CodeForge - منشئ المشاريع البرمجية"""
    print_colored_logo()
def print_logo():
    """طباعة شعار CodeForge الملون"""
    logo = f"""
{Fore.BLUE}╔═══════════════════════════════════════════════════════╗{Style.RESET_ALL}
{Fore.BLUE}║{Style.RESET_ALL}                                                       {Fore.BLUE}║{Style.RESET_ALL}
{Fore.BLUE}║{Style.RESET_ALL}    {Fore.CYAN}   _____          ______               {Style.RESET_ALL}      {Fore.BLUE}║{Style.RESET_ALL}
{Fore.BLUE}║{Style.RESET_ALL}    {Fore.CYAN}  / ____|        |  ____|              {Style.RESET_ALL}      {Fore.BLUE}║{Style.RESET_ALL}
{Fore.BLUE}║{Style.RESET_ALL}    {Fore.CYAN} | |     ___   __| |__ _ __ ___  ___   {Style.RESET_ALL}      {Fore.BLUE}║{Style.RESET_ALL}
{Fore.BLUE}║{Style.RESET_ALL}    {Fore.CYAN} | |    / _ \\ / _`  __| '__/ _ \\/ _ \\  {Style.RESET_ALL}      {Fore.BLUE}║{Style.RESET_ALL}
{Fore.BLUE}║{Style.RESET_ALL}    {Fore.CYAN} | |___| (_) | (_| |  | | |  __/  __/  {Style.RESET_ALL}      {Fore.BLUE}║{Style.RESET_ALL}
{Fore.BLUE}║{Style.RESET_ALL}    {Fore.CYAN}  \\_____\\___/ \\__,_|  |_|  \\___|\\___|  {Style.RESET_ALL}      {Fore.BLUE}║{Style.RESET_ALL}
{Fore.BLUE}║{Style.RESET_ALL}                                                       {Fore.BLUE}║{Style.RESET_ALL}
{Fore.BLUE}║{Style.RESET_ALL}        {Fore.YELLOW}🔨 {Style.BRIGHT}The Code Forge{Style.RESET_ALL}                        {Fore.BLUE}║{Style.RESET_ALL}
{Fore.BLUE}║{Style.RESET_ALL}        {Fore.WHITE}From Idea to Deployment{Style.RESET_ALL}                   {Fore.BLUE}║{Style.RESET_ALL}
{Fore.BLUE}║{Style.RESET_ALL}                                                       {Fore.BLUE}║{Style.RESET_ALL}
{Fore.BLUE}╚═══════════════════════════════════════════════════════╝{Style.RESET_ALL}
    """
    print(logo)

def print_header():
    """رأس الصفحة مع المعلومات"""
    from codeforge import __version__
    
    header = f"""
{Fore.YELLOW}┌─────────────────────────────────────────────────────┐{Style.RESET_ALL}
{Fore.YELLOW}│{Style.RESET_ALL}     {Style.BRIGHT}🚀 CodeForge v{__version__} - منشئ المشاريع البرمجية {Style.RESET_ALL}    {Fore.YELLOW}│{Style.RESET_ALL}
{Fore.YELLOW}│{Style.RESET_ALL}     {Fore.CYAN}https://github.com/Abdullahreda1969/codeforge{Style.RESET_ALL}     {Fore.YELLOW}│{Style.RESET_ALL}
{Fore.YELLOW}└─────────────────────────────────────────────────────┘{Style.RESET_ALL}
    """
    print(header)

@click.group()
def cli():
    """CodeForge - منشئ المشاريع البرمجية"""
    print_logo()
    print_header()

# باقي الأوامر تبقى كما هي...
@cli.command()
def version():
    """عرض إصدار CodeForge"""
    from codeforge import print_version
    print_version()

# ... باقي الأوامر

@cli.command()
def version():
    """عرض إصدار CodeForge"""
    from codeforge import print_version

    print_version()

@cli.command()
@click.argument('template')
@click.argument('project_name')
@click.option('--author', '-a', default='مطور CodeForge', help='اسم المؤلف')
@click.option('--year', '-y', default='2024', help='سنة الإنشاء')
def create(template, project_name, author, year):
    """إنشاء مشروع جديد"""
    click.echo(f'🚀 جاري إنشاء {project_name}...')
    
    engine = TemplateEngine()
    
    success = engine.create_project(
        template_name=template,
        project_name=project_name,
        data={
            "author": author,
            "year": year
        }
    )
    
    if success:
        click.echo(f'✅ تم إنشاء {project_name} بنجاح!')
        click.echo(f'📁 cd {project_name}')
    else:
        click.echo(f'❌ فشل إنشاء المشروع')
        raise click.Abort()

@cli.command()
def list_templates():
    """عرض القوالب المتاحة"""
    engine = TemplateEngine()
    templates = engine.get_templates()
    
    if templates:
        click.echo("📁 القوالب المتاحة:")
        for template in templates:
            click.echo(f"  • {template}")
    else:
        click.echo("📭 لا توجد قوالب متاحة")

if __name__ == "__main__":
    cli()