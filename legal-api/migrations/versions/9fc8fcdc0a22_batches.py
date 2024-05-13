"""batches

Revision ID: 9faa0630c3f9
Revises: f4f93ea8887e
Create Date: 2024-05-01 10:29:37.327296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fc8fcdc0a22'
down_revision = 'f4f93ea8887e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('batches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('batch_type', sa.Enum('INVOLUNTARY_DISSOLUTION', name='batch_type'), nullable=False),
    sa.Column('status', sa.Enum('HOLD', 'PROCESSING', 'COMPLETED', 'CANCELLED', 'ERROR', name='batch_status'), nullable=False),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('end_date', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('notes', sa.VARCHAR(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('batch_processing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('batch_id', sa.Integer(), nullable=False),
    sa.Column('business_id', sa.Integer(), nullable=False),
    sa.Column('business_identifier', sa.VARCHAR(10), nullable=False),
    sa.Column('step', sa.Enum('WARNING_LEVEL_1', 'WARNING_LEVEL_2', 'DISSOLUTION', name='batch_processing_step'), nullable=False),
    sa.Column('status', sa.Enum('HOLD', 'PROCESSING', 'WITHDRAWN', 'COMPLETED', 'ERROR', name='batch_processing_status'), nullable=False),
    sa.Column('notes', sa.VARCHAR(length=150), nullable=True),
    sa.Column('created_date', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('last_modified', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['batch_id'], ['batches.id']),
    sa.ForeignKeyConstraint(['business_id'], ['businesses.id']),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('batch_processing')
    op.execute("DROP TYPE batch_processing_step;")
    op.execute("DROP TYPE batch_processing_status;")
    op.drop_table('batches')
    op.execute("DROP TYPE batch_type;")
    op.execute("DROP TYPE batch_status;")

    # ### end Alembic commands ###