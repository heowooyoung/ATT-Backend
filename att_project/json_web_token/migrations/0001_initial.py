# Generated by Django 5.0.7 on 2024-08-09

# Migrations를 정의하는 클래스로 Django에서 자동으로 생성
from django.db import migrations, models

# Migration File이 json_web_token 앱에서 처음 실행되는 마이그레이션임을 나타냄
class Migration(migrations.Migration):
    initial = True

    # 이 마이그레이션이 의존하는 다른 마이그레이션을 정의
    # "auth" 앱의 "0012_alter_user_first_name_max_length" 마이그레이션 이후에 실행
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    # 이 마이그레이션에서 수행할 작업 목록
    operations = [
        # 새로운 모델 (Table)을 생성하는 작업을 정의
        migrations.CreateModel(
            # 생성할 모델 (Table)의 이름을 "User"로 정의
            name="User",
            # 이 모델 (Table)에 포함될 필드들을 정의
            fields=[
                # id 필드: PRIMARY_KEY로 사용되며, id가 자동으로 증가하는 AutoField를 적용
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),

                # password 필드: 사용자의 비밀번호를 저장
                ("password", models.CharField(max_length=128, verbose_name="password")),

                # last_login 필드: 사용자가 마지막으로 로그인한 시간을 저장
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),

                # email 필드: 사용자의 이메일 주소를 저장하고 고유값(Unique)으로 설정
                ("email", models.EmailField(max_length=255, unique=True)),

                # is_active 필드: 사용자가 활성 상태인지 여부를 나타내며, 기본값을 True로 설정
                ("is_active", models.BooleanField(default=True)),

                # is_staff 필드: 관리 사이트 접근 권한이 있는지 여부를 나타내며, 기본값은 False로 설정
                ("is_staff", models.BooleanField(default=False)),

                # is_superuser 필드: 슈퍼유저 권한을 가지고 있는지 여부를 나타내며, 기본값을 False로 설정
                ("is_superuser", models.BooleanField(default=False)),

                # created_at 필드: 사용자가 생성된 날짜와 시간을 자동으로 기록
                ("created_at", models.DateTimeField(auto_now_add=True)),

                # updated_at 필드: 사용자가 마지막으로 수정된 날짜와 시간을 자동으로 기록
                ("updated_at", models.DateTimeField(auto_now=True)),

                # groups 필드: 사용자가 속한 그룹들을 ManyToMany 관계로 정의하며,
                # 이 필드는 Django의 기본 권한 관리 시스템과 연동됨
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                # user_permissions 필드: 사용자가 가진 개별 권한들을 ManyToMany 관계로 정의하며,
                # 이 필드 역시 Django의 기본 권한 관리 시스템과 연동됨
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            # 이 모델 (Table)은 데이터베이스에 실제 테이블로 생성됨을 나타냄
            options={
                "abstract": False,
            },
        ),
    ]