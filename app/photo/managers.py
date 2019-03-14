from django.db.models import Manager, Q

class PhotoManager(Manager):
    
    def get_query_set(self):
        qs = super(PhotoManager, self).get_query_set()
        return qs

    def get_accepted(self):
        return self.all().filter(is_accepted=True)
    
    def get_queryset_by_user(self, user):
        qs = self.all()
        if user.is_superuser:
            return qs
        q = Q(author=user) | Q(is_accepted=True)
        return qs.filter(q)