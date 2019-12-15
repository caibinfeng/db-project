"""empty message

Revision ID: 753febe98817
Revises: b1b1001ca6b2
Create Date: 2019-12-15 21:03:22.181881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '753febe98817'
down_revision = 'b1b1001ca6b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comment_ibfk_3', 'comment', type_='foreignkey')
    op.create_foreign_key(None, 'comment', 'order', ['order_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.create_foreign_key('comment_ibfk_3', 'comment', 'goods', ['order_id'], ['id'])
    # ### end Alembic commands ###
