# Generated by Django 3.0.3 on 2020-05-06 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField()),
                ('row_number', models.IntegerField()),
                ('SEQUENCE_ID', models.CharField(max_length=1000)),
                ('SEQUENCE_INPUT', models.CharField(max_length=1000)),
                ('FUNCTIONAL', models.CharField(max_length=1000)),
                ('IN_FRAME', models.CharField(max_length=1000)),
                ('STOP', models.CharField(max_length=1000)),
                ('MUTATED_INVARIANT', models.CharField(max_length=1000)),
                ('INDELS', models.CharField(max_length=1000)),
                ('V_CALL', models.CharField(max_length=1000)),
                ('D_CALL', models.CharField(max_length=1000)),
                ('J_CALL', models.CharField(max_length=1000)),
                ('SEQUENCE_VDJ', models.CharField(max_length=1000)),
                ('SEQUENCE_IMGT', models.CharField(max_length=1000)),
                ('V_SEQ_START', models.CharField(max_length=1000)),
                ('V_SEQ_LENGTH', models.CharField(max_length=1000)),
                ('V_GERM_START_VDJ', models.CharField(max_length=1000)),
                ('V_GERM_LENGTH_VDJ', models.CharField(max_length=1000)),
                ('V_GERM_START_IMGT', models.CharField(max_length=1000)),
                ('V_GERM_LENGTH_IMGT', models.CharField(max_length=1000)),
                ('NP1_LENGTH', models.CharField(max_length=1000)),
                ('D_SEQ_START', models.CharField(max_length=1000)),
                ('D_SEQ_LENGTH', models.CharField(max_length=1000)),
                ('D_GERM_START', models.CharField(max_length=1000)),
                ('D_GERM_LENGTH', models.CharField(max_length=1000)),
                ('NP2_LENGTH', models.CharField(max_length=1000)),
                ('J_SEQ_START', models.CharField(max_length=1000)),
                ('J_SEQ_LENGTH', models.CharField(max_length=1000)),
                ('J_GERM_START', models.CharField(max_length=1000)),
                ('J_GERM_LENGTH', models.CharField(max_length=1000)),
                ('JUNCTION', models.CharField(max_length=1000)),
                ('JUNCTION_LENGTH', models.CharField(max_length=1000)),
                ('GERMLINE_IMGT', models.CharField(max_length=1000)),
                ('FWR1_IMGT', models.CharField(max_length=1000)),
                ('FWR2_IMGT', models.CharField(max_length=1000)),
                ('FWR3_IMGT', models.CharField(max_length=1000)),
                ('FWR4_IMGT', models.CharField(max_length=1000)),
                ('CDR1_IMGT', models.CharField(max_length=1000)),
                ('CDR2_IMGT', models.CharField(max_length=1000)),
                ('CDR3_IMGT', models.CharField(max_length=1000)),
                ('CDR3_IGBLAST', models.CharField(max_length=1000)),
                ('CDR3_IGBLAST_AA', models.CharField(max_length=1000)),
                ('PRCONS', models.CharField(max_length=1000)),
                ('SEQORIENT', models.CharField(max_length=1000)),
                ('PRIMER', models.CharField(max_length=1000)),
                ('ISOTYPE', models.CharField(max_length=1000)),
                ('CONSCOUNT', models.CharField(max_length=1000)),
                ('DUPCOUNT', models.CharField(max_length=1000)),
                ('DUPCOUNT_NEW', models.CharField(max_length=1000)),
                ('CLONE', models.CharField(max_length=1000)),
                ('GERMLINE_V_CALL', models.CharField(max_length=1000)),
                ('GERMLINE_D_CALL', models.CharField(max_length=1000)),
                ('GERMLINE_J_CALL', models.CharField(max_length=1000)),
                ('MUT', models.CharField(max_length=1000)),
                ('CLONE_SIZE', models.CharField(max_length=1000)),
            ],
        ),
    ]
