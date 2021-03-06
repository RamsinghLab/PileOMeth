from subprocess import check_call
import os
import os.path as op

def rm(f):
    try:
        os.unlink(f)
    except OSError:
        pass

rm('po')
check_call('gcc ../PileOMeth.c ../bed.c -lhts -lz -o po', shell=True)
assert op.exists('po')

rm('ct_aln_CpG.bedGraph')
check_call('./po ct100.fa ct_aln.bam -q 2', shell=True)
assert op.exists('ct_aln_CpG.bedGraph')
lines = sum(1 for _ in open('ct_aln_CpG.bedGraph'))
assert lines == 1



rm('cg_aln_CpG.bedGraph')
check_call('./po cg100.fa cg_aln.bam -q 2', shell=True)
assert op.exists('cg_aln_CpG.bedGraph')
lines = sum(1 for _ in open('cg_aln_CpG.bedGraph'))
assert lines > 1

# should be none with q > 10
check_call('./po cg100.fa cg_aln.bam -q 10', shell=True)
assert op.exists('cg_aln_CpG.bedGraph')
lines = sum(1 for _ in open('cg_aln_CpG.bedGraph'))
assert lines == 1
