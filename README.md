## poc-Sidekicks

Entry point for new Fedora Project packagers

list official Fedora Project packagers with only one maintainer

For reference, check [this link](https://fedoraproject.org/wiki/Policy_for_encouraging_comaintainers_of_packages)

### Badges idea:

sidekick I, II, III

"You became a co-maintainer of a package with less than 3 co-maintainers or of a branch with a single commiter".

For 1, 5 and 10 packages. This number should not scale up since [we do not want people to comaintain too many packages](https://fedoraproject.org/wiki/Policy_for_encouraging_comaintainers_of_packages#Don.27t_.28co-.29maintain_too_many_packages)


### Using the pkgdb API

GET https://admin.fedoraproject.org/pkgdb/api/packages/?[params]

##### params should contain:

* limit: 500 (max)
* acls: True
* status: Approved
* branches: master, f25, f24, f23, epel7, epel6
* page: navigate from 1 to the last one

https://admin.fedoraproject.org/pkgdb/api/monitored?format=json
* returns a list with all packages in anitya, mark those as 'monitored' or sth
* we could also check on anitya API if package is up to date
* note that pkgdb api will not provide info on package versions
