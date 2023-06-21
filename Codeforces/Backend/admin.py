from django.contrib import admin
from .models import (CodeforcesUser, BlogEntry, Comment,
					 RecentAction ,RatingChange,Contest,
					 Problem,ProblemStatistics,ContestAuthors,
					 Member,Party,PartyMember,ProblemTag,
					 Submission,Hack,ProblemResult,BlogTags

					 )
# Register your models here.

admin.site.register(CodeforcesUser)
admin.site.register(BlogEntry)
admin.site.register(Comment)
admin.site.register(RecentAction)
admin.site.register(RatingChange)
admin.site.register(Contest)
admin.site.register(Problem)
admin.site.register(ProblemStatistics)
admin.site.register(ContestAuthors)
admin.site.register(Member)
admin.site.register(Party)
admin.site.register(PartyMember)
admin.site.register(ProblemTag)
admin.site.register(Submission)
admin.site.register(Hack)
admin.site.register(ProblemResult)
admin.site.register(BlogTags)
