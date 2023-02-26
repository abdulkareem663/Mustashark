# Generated by Django 4.1.6 on 2023-02-07 11:38

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Center", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Description",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "img",
                    models.ImageField(
                        blank=True, null=True, upload_to="blog/description/"
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("body", ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name="SEO",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("head", models.CharField(max_length=250)),
                ("description", models.TextField(blank=True, null=True)),
                ("img", models.ImageField(blank=True, null=True, upload_to="blog/")),
                ("keyword", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="task_project_desc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.description",
                    ),
                ),
                (
                    "seo",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.seo"
                    ),
                ),
                (
                    "task_project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Center.taskproject",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="subject_desc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.description",
                    ),
                ),
                (
                    "seo",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.seo"
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Center.subject"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="spiecification_desc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.description",
                    ),
                ),
                (
                    "seo",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.seo"
                    ),
                ),
                (
                    "spiecification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Center.spiecification",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="service_desc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.description",
                    ),
                ),
                (
                    "seo",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.seo"
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Center.service"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="project_desc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.description",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Center.project"
                    ),
                ),
                (
                    "seo",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.seo"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="degree_desc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "degree",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Center.degree"
                    ),
                ),
                (
                    "description",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.description",
                    ),
                ),
                (
                    "seo",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.seo"
                    ),
                ),
            ],
        ),
    ]