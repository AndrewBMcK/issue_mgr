# Generated by Django 5.0.1 on 2024-01-21 18:40

from django.db import migrations

def populate_role(apps, schemaeditor):
    entries = {
        "developer": "A person on the team who works on issues",
        "scrum master": "The scrum team's coach",
        "product owner": "The person responsible for creating issues"
    }
    Role = apps.get_model("accounts", "Role")
    for key, value in entries.items():
        role_obj = Role(name=key, description=value)
        role_obj.save()

def populate_team(apps, schemaeditor):
    entries = {
        "alpha": "The A team",
        "bravo": "The B team",
        "charlie": "The C team",
        "delta": "The D team"
    }
    Team = apps.get_model("accounts", "Team")
    for key, value in entries.items():
        team_obj = Team(name=key, description=value)
        team_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_role),
        migrations.RunPython(populate_team),
    ]
