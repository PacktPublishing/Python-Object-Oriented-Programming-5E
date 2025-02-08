# Use `make test TOX_OPTIONS='-r'` to refresh all chapter virtual environments
.phony : test

TOX_OPTIONS=

test :
	cd ch_01 && tox $(TOX_OPTIONS)
	cd ch_02 && tox $(TOX_OPTIONS)
	cd ch_03 && tox $(TOX_OPTIONS)
	cd ch_04 && tox $(TOX_OPTIONS)
	cd ch_05 && tox $(TOX_OPTIONS)
	cd ch_06 && tox $(TOX_OPTIONS)
	cd ch_07 && tox $(TOX_OPTIONS)
	# cd ch_08 && tox $(TOX_OPTIONS)
	# cd ch_09 && tox $(TOX_OPTIONS)
	# cd ch_10 && tox $(TOX_OPTIONS) && tox -e bench
	# cd ch_11 && tox $(TOX_OPTIONS)
	# cd ch_12 && tox $(TOX_OPTIONS)
	# cd ch_13 && tox $(TOX_OPTIONS) && tox -e coverage
	# cd ch_14 && tox $(TOX_OPTIONS)
