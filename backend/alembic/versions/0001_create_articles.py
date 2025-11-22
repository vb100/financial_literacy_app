"""create articles table"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0001_create_articles"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "article",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("feed_date", sa.Date(), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("url", sa.Text(), nullable=False),
        sa.Column("source", sa.Text(), nullable=True),
        sa.Column("snippet", sa.Text(), nullable=True),
        sa.Column("summary", sa.Text(), nullable=True),
        sa.Column("published_at", sa.DateTime(), nullable=True),
        sa.Column("rank", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("feed_date", "url", name="uq_feed_date_url"),
        sa.UniqueConstraint("feed_date", "rank", name="uq_feed_date_rank"),
    )
    op.create_index("idx_feed_date_rank", "article", ["feed_date", "rank"])
    op.create_index("idx_feed_date_created", "article", ["feed_date", "created_at"])


def downgrade() -> None:
    op.drop_index("idx_feed_date_created", table_name="article")
    op.drop_index("idx_feed_date_rank", table_name="article")
    op.drop_table("article")
