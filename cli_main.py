"""
واجهة CLI لـ CodeForge
"""

import sys
import os

# أضف src إلى المسار
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.insert(0, src_path)

import click
from codeforge import print_version
from codeforge.modules.scaffolder.engine import TemplateEngine

@click.group()
def cli():
    """CodeForge - منشئ المشاريع البرمجية"""
    pass

@cli.command()
def version():
    """عرض إصدار CodeForge"""
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