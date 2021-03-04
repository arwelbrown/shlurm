import app.py

db.session.query(Shlurm).delete()
deb.session.commit()

db.create_all()


big_Shlurm = Shlurm.query.all()
shlurm_fed_list = [big_Shlurm.pop().time_fed]
shlurm_fed = shlurm_fed_list
# total_fed = 0
total_fed = Shlurm.query.count()

# ALONG THESE LINES