from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class CodeforcesUser(models.Model):
    handle = models.CharField(max_length=255, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    vkId = models.CharField(max_length=255, blank=True)
    openId = models.CharField(max_length=255, blank=True)
    firstName = models.CharField(max_length=255, blank=True, null=True)
    lastName = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    contribution = models.IntegerField(default = 0)
    rank = models.CharField(max_length=255)
    rating = models.IntegerField(default = 800)
    maxRank = models.CharField(max_length=255)
    maxRating = models.IntegerField(default = "800")
    lastOnlineTime = models.DateTimeField(default=timezone.now)
    registrationTime = models.DateTimeField(default=timezone.now)
    friendOfCount = models.IntegerField(default = 0, null = False)
    avatar = models.URLField(null = True)
    titlePhoto = models.URLField(null = True)

    def __str__(self):
        return f"User {self.handle}"
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        # ordering = ["id"]


class BlogEntry(models.Model):
    id = models.IntegerField(primary_key=True)
    originalLocale = models.CharField(max_length=255)
    creationTimeSeconds = models.DateTimeField(default=timezone.now)
    authorHandle = models.ForeignKey('CodeforcesUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    locale = models.CharField(max_length=255)
    modificationTimeSeconds = models.DateTimeField(auto_now=True)
    allowViewHistory = models.BooleanField()
    rating = models.IntegerField()

    def __str__(self):
        return f"BlogEntry {self.id}"
    class Meta:
        verbose_name = 'BlogEntry'
        verbose_name_plural = 'BlogEntries'
        ordering = ["id"]

class BlogTags(models.Model):
    id = models.ForeignKey('BlogEntry', on_delete=models.CASCADE, primary_key=True)
    tag = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.tag}"

    class Meta:
        verbose_name = 'Blog Tag'
        verbose_name_plural = 'Blog Tags'
        unique_together = ('id', 'tag')

class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    creationTimeSeconds = models.DateTimeField(auto_now_add=True)
    commentatorHandle = models.ForeignKey('CodeforcesUser', on_delete=models.CASCADE)
    locale = models.CharField(max_length=255)
    text = models.TextField()
    parentCommentId = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField()

    def __str__(self):
        return f"Comment {self.id}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class RecentAction(models.Model):
    timeSeconds = models.DateTimeField(default=timezone.now)
    blogEntryId = models.ForeignKey('BlogEntry', on_delete=models.CASCADE)
    commentId = models.ForeignKey('Comment', on_delete=models.CASCADE)

    def __str__(self):
        return f"RecentAction {self.id}"

    class Meta:
        verbose_name = 'Recent Action'
        verbose_name_plural = 'Recent Actions'
        constraints = [
            models.UniqueConstraint(fields=['blogEntryId', 'commentId'], name='unique_recent_action')
        ]

class RatingChange(models.Model):
    contestId = models.IntegerField(primary_key=True)
    contestName = models.CharField(max_length=255,unique=True)
    handle = models.ForeignKey('CodeforcesUser', to_field='handle', on_delete=models.CASCADE)
    rank = models.IntegerField()
    ratingUpdateTimeSeconds = models.DateTimeField(default=timezone.now)
    oldRating = models.IntegerField()
    newRating = models.IntegerField()

    def __str__(self):
        return f"RatingChange {self.contestId}"

    class Meta:
        verbose_name = 'Rating Change'
        verbose_name_plural = 'Rating Changes'


class Contest(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=[('CF', 'Codeforces'), ('IOI', 'IOI'), ('ICPC', 'ICPC')])
    phase = models.CharField(max_length=20, choices=[('BEFORE', 'Before'), ('CODING', 'Coding'), ('PENDING_SYSTEM_TEST', 'Pending System Test'), ('SYSTEM_TEST', 'System Test'), ('FINISHED', 'Finished')])
    frozen = models.BooleanField()
    durationSeconds = models.IntegerField()
    startTimeSeconds = models.IntegerField(blank=True, null=True)
    relativeTimeSeconds = models.IntegerField(blank=True, null=True)
    websiteUrl = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    difficulty = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    kind = models.CharField(max_length=255, blank=True, null=True)
    icpcRegion = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    season = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Contest {self.id}"

    class Meta:
        verbose_name = 'Contest'
        verbose_name_plural = 'Contests'

class ContestAuthors(models.Model):
    contestId = models.ForeignKey('Contest', on_delete=models.CASCADE)
    authorHandle = models.ForeignKey('CodeforcesUser', on_delete=models.CASCADE)

    def __str__(self):
        return f"Contest: {self.contestId}, Author: {self.authorHandle}"

    class Meta:
        verbose_name = 'Contest Author'
        verbose_name_plural = 'Contest Authors'
        constraints = [
            models.UniqueConstraint(fields=['contestId', 'authorHandle'], name='unique_contest_author')
        ]

class Member(models.Model):
    handle = models.OneToOneField('CodeforcesUser', primary_key=True, on_delete=models.CASCADE)
    member = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Handle: {self.handle}, Member: {self.member}"

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

class Party(models.Model):
    contestId = models.ForeignKey('Contest', primary_key=True, on_delete=models.CASCADE)
    participantType = models.CharField(max_length=20, choices=[
        ('CONTESTANT', 'Contestant'),
        ('PRACTICE', 'Practice'),
        ('VIRTUAL', 'Virtual'),
        ('MANAGER', 'Manager'),
        ('OUT_OF_COMPETITION', 'Out of Competition'),
    ])
    teamId = models.IntegerField(blank=True, null=True)
    teamName = models.CharField(max_length=255, blank=True, null=True)
    ghost = models.BooleanField()
    room = models.IntegerField(blank=True, null=True)
    startTimeSeconds = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return f"Contest ID: {self.contestId}, Participant Type: {self.participantType}"

    class Meta:
        verbose_name = 'Party'
        verbose_name_plural = 'Parties'
    
class PartyMember(models.Model):
    contestId = models.ForeignKey('Party', on_delete=models.CASCADE)
    handle = models.ForeignKey('Member', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['contestId', 'handle'], name='unique_party_member')
        ]


class Problem(models.Model):
    contestId = models.ForeignKey('Contest',to_field = "id" ,on_delete=models.CASCADE, blank=True)
    problemsetName = models.CharField(max_length=255, blank=True, null=True)
    index = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=[('PROGRAMMING', 'Programming'), ('QUESTION', 'Question')])
    points = models.FloatField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Problem {self.contestId}-{self.index}"

    class Meta:
        verbose_name = 'Problem'
        verbose_name_plural = 'Problems'
        unique_together = ('contestId', 'index')

class ProblemTag(models.Model):
    contestId = models.ForeignKey('Problem', on_delete=models.CASCADE, related_name='problem_tags')
    index = models.ForeignKey('Problem', on_delete=models.CASCADE, related_name='problem_tags_index')
    tag = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['contestId', 'index', 'tag'], name='unique_problem_tag')
        ]
        db_table = 'problemtag'

class ProblemStatistics(models.Model):
    contestId = models.ForeignKey('Problem', on_delete=models.CASCADE, related_name='statistics')
    index = models.ForeignKey('Problem', on_delete=models.CASCADE)
    solvedCount = models.IntegerField()

    def __str__(self):
        return f"ProblemStatistics {self.contestId}-{self.index}"

    class Meta:
        verbose_name = 'Problem Statistics'
        verbose_name_plural = 'Problem Statistics'
        unique_together = ('contestId', 'index')


class Submission(models.Model):
    id = models.IntegerField(primary_key=True)
    contestId = models.ForeignKey('Problem', on_delete=models.CASCADE, related_name='problem_submissions')
    creationTimeSeconds = models.DateTimeField(auto_now_add=True)
    relativeTimeSeconds = models.IntegerField()
    index = models.ForeignKey('Problem', on_delete=models.CASCADE, related_name='problem_submissions_with_index')
    author = models.ForeignKey('PartyMember', on_delete=models.CASCADE, related_name='submissions')
    programmingLanguage = models.CharField(max_length=255)
    verdict = models.CharField(
        max_length=100,
        choices=[
            ('FAILED', 'FAILED'),
            ('OK', 'OK'),
            ('PARTIAL', 'PARTIAL'),
            ('COMPILATION_ERROR', 'COMPILATION_ERROR'),
            ('RUNTIME_ERROR', 'RUNTIME_ERROR'),
            ('WRONG_ANSWER', 'WRONG_ANSWER'),
            ('PRESENTATION_ERROR', 'PRESENTATION_ERROR'),
            ('TIME_LIMIT_EXCEEDED', 'TIME_LIMIT_EXCEEDED'),
            ('MEMORY_LIMIT_EXCEEDED', 'MEMORY_LIMIT_EXCEEDED'),
            ('IDLENESS_LIMIT_EXCEEDED', 'IDLENESS_LIMIT_EXCEEDED'),
            ('SECURITY_VIOLATED', 'SECURITY_VIOLATED'),
            ('CRASHED', 'CRASHED'),
            ('INPUT_PREPARATION_CRASHED', 'INPUT_PREPARATION_CRASHED'),
            ('CHALLENGED', 'CHALLENGED'),
            ('SKIPPED', 'SKIPPED'),
            ('TESTING', 'TESTING'),
            ('REJECTED', 'REJECTED'),
        ],
        null=True
    )
    testset = models.CharField(
        max_length=10,
        choices=[
            ('SAMPLES', 'SAMPLES'),
            ('PRETESTS', 'PRETESTS'),
            ('TESTS', 'TESTS'),
            ('CHALLENGES', 'CHALLENGES'),
            ('TESTS1', 'TESTS1'),
            ('TESTS2', 'TESTS2'),
            ('TESTS3', 'TESTS3'),
            ('TESTS4', 'TESTS4'),
            ('TESTS5', 'TESTS5'),
            ('TESTS6', 'TESTS6'),
            ('TESTS7', 'TESTS7'),
            ('TESTS8', 'TESTS8'),
            ('TESTS9', 'TESTS9'),
            ('TESTS10', 'TESTS10'),
        ],
        null=True
    )
    passedTestCount = models.IntegerField()
    timeConsumedMillis = models.IntegerField()
    memoryConsumedBytes = models.IntegerField()
    points = models.FloatField(null=True)
    class Meta:
        verbose_name = 'Problem Submission'
        verbose_name_plural = 'Problem Submissions'


class Hack(models.Model):
    HACK_SUCCESSFUL = 'SUCCESSFUL'
    HACK_UNSUCCESSFUL = 'UNSUCCESSFUL'
    INVALID_INPUT = 'INVALID_INPUT'
    GENERATOR_INCOMPILABLE = 'GENERATOR_INCOMPILABLE'
    GENERATOR_CRASHED = 'GENERATOR_CRASHED'
    IGNORED = 'IGNORED'
    TESTING = 'TESTING'
    OTHER = 'OTHER'

    VERDICT_CHOICES = [
        ('SUCCESSFUL', 'Successful Hack'),
        ('UNSUCCESSFUL', 'Unsuccessful Hack'),
        ('INVALID_INPUT', 'Invalid Input'),
        ('GENERATOR_INCOMPILABLE', 'Generator Incompilable'),
        ('GENERATOR_CRASHED', 'Generator Crashed'),
        ('IGNORED', 'Ignored'),
        ('TESTING', 'Testing'),
        ('OTHER', 'Other'),
    ]

    id = models.IntegerField(primary_key=True)
    creationTimeSeconds = models.DateTimeField(auto_now_add=True)
    hacker = models.ForeignKey('CodeforcesUser', on_delete=models.CASCADE, related_name='hacks_made')
    defender = models.ForeignKey('CodeforcesUser', on_delete=models.CASCADE, related_name='hacks_received')
    verdict = models.CharField(max_length=100, choices=VERDICT_CHOICES, null=True, blank=True)
    contestId = models.ForeignKey('Problem', on_delete=models.CASCADE, related_name='problem_hacks_contest')
    index = models.ForeignKey('Problem', on_delete=models.CASCADE, related_name='problem_hacks_index')
    test = models.CharField(max_length=255, null=True, blank=True)
    judgeProtocol = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'hack'
        verbose_name = 'Hack'
        verbose_name_plural = 'Hacks'

    def __str__(self):
        return f"Hack {self.id}"


class ProblemResult(models.Model):
    PRELIMINARY = 'PRELIMINARY'
    FINAL = 'FINAL'

    TYPE_CHOICES = [
        ('PRELIMINARY', 'Preliminary'),
        ('FINAL', 'Final'),
    ]

    id = models.IntegerField(primary_key=True)
    points = models.FloatField()
    penalty = models.IntegerField(null=True, blank=True)
    rejectedAttemptCount = models.IntegerField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    bestSubmissionTimeSeconds = models.IntegerField(null=True, blank=True)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'problem_result'
        verbose_name = 'Problem Result'
        verbose_name_plural = 'Problem Results'

    def __str__(self):
        return f"Problem Result {self.id}"