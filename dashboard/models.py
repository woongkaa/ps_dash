# -*- coding: utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.

from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_init
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


class AdDailyTbl(models.Model):
    # id = models.AutoField(primary_key=True)
    date = models.DateField()
    ad_key = models.IntegerField()
    ad_hit = models.IntegerField()
    uv_hit = models.IntegerField()
    link_click = models.IntegerField()
    post_count = models.IntegerField()
    mp3_click = models.IntegerField()
    album_click = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'ad_daily_tbl'


class AdTbl(models.Model):
    ad_key = models.IntegerField(primary_key=True)
    ad_type = models.CharField(max_length=1)
    video_type = models.CharField(max_length=1)
    ad_artist = models.TextField()
    ad_title = models.TextField()
    ad_content = models.TextField()
    ad_youtubeid = models.TextField()
    ad_n_video_mobile = models.TextField()
    ad_n_video = models.TextField()
    ad_n_page = models.TextField()
    ad_n_play = models.TextField()
    movie_time = models.IntegerField()
    uv_time = models.IntegerField()
    movie_time_m = models.IntegerField()
    uv_time_m = models.IntegerField()
    event_link = models.TextField()
    book_link = models.TextField()
    ad_movieurl = models.TextField()
    ad_link = models.TextField()
    ad_ownerkey = models.IntegerField()
    ad_hit = models.IntegerField()
    uv_hit = models.IntegerField()
    thumb = models.TextField()
    ad_thumbnail = models.TextField()
    ad_thumbnail_post = models.TextField()
    ad_poster = models.TextField()
    mp3_click = models.IntegerField()
    album_click = models.IntegerField()
    intro = models.TextField()
    intro_new = models.TextField()
    news = models.TextField()
    news_m = models.TextField()
    music_list = models.TextField()
    musiclist_and = models.TextField()
    bugs = models.TextField()
    melon_ios = models.TextField()
    melon_and = models.TextField()
    album_list = models.TextField()
    ad_limit = models.IntegerField()
    post_count = models.IntegerField()
    income_data = models.IntegerField()
    income = models.IntegerField()
    s_income = models.IntegerField()
    expired = models.IntegerField()
    survey_good = models.IntegerField()
    survey_bad = models.IntegerField()
    survey_total = models.IntegerField()
    survey_good_str = models.CharField(max_length=60)
    survey_bad_str = models.CharField(max_length=60)

    class Meta:
        # managed = False
        db_table = 'ad_tbl'
        ordering = ['-ad_key']

    def __unicode__(self):
        return u"[%s] %s" % (self.ad_key, self.ad_title)

    def get_daily_logs(self):
        try:
            logs = DailyLog.objects.filter(movie=self)
        except ObjectDoesNotExist:
            logs = None
        return logs


class AdvertiserReq(models.Model):
    index = models.IntegerField(primary_key=True)
    user_key = models.IntegerField()
    req_date = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'advertiser_req'


class AdwTbl(models.Model):
    key = models.IntegerField(primary_key=True)
    adkey = models.IntegerField()
    fb_id = models.TextField()
    ad_hash = models.TextField()
    post_id = models.TextField()
    hit = models.IntegerField()
    uv_hit = models.IntegerField()
    survey_total = models.IntegerField()
    survey_good = models.IntegerField()
    survey_bad = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'adw_tbl'


class AnaUser(models.Model):
    user_id = models.IntegerField()
    sex = models.CharField(max_length=11)
    age = models.IntegerField()
    genre = models.TextField()
    fb = models.IntegerField()
    kakao = models.IntegerField()
    story = models.IntegerField()
    clip = models.IntegerField()
    pattern = models.IntegerField()
    power = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'ana_user'


class BoardTbl(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ismovie = models.IntegerField(db_column='isMovie')  # Field name made lowercase.
    title = models.TextField()
    contents = models.TextField()
    movie_title = models.TextField()
    price = models.IntegerField()
    isvisible = models.IntegerField(db_column='isVisible')  # Field name made lowercase.
    input_time = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'board_tbl'


class FbUsrTbl(models.Model):
    user_key = models.IntegerField(primary_key=True)
    fb_id = models.CharField(unique=True, max_length=20)
    name = models.TextField()
    email = models.TextField()
    age = models.IntegerField()
    gender = models.TextField()
    birth = models.TextField()
    total_income = models.IntegerField()
    income = models.IntegerField()
    sv_income = models.IntegerField()
    sv = models.IntegerField()
    friends_count = models.IntegerField()
    recommender = models.TextField()

    class Meta:
        # managed = False
        db_table = 'fb_usr_tbl'


class FriendTbl(models.Model):
    from_user_key = models.IntegerField()
    to_user_key = models.IntegerField()
    isaccepted = models.CharField(db_column='isAccepted', max_length=1)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'friend_tbl'


class GcmUsrTbl(models.Model):
    fb_id = models.CharField(unique=True, max_length=20)
    gcm_id = models.CharField(max_length=200, blank=True)

    class Meta:
        # managed = False
        db_table = 'gcm_usr_tbl'


class MarketTbl(models.Model):
    item_key = models.IntegerField()
    price = models.IntegerField()
    title = models.TextField()
    description = models.TextField()
    img_src = models.TextField()

    class Meta:
        # managed = False
        db_table = 'market_tbl'


class MemberTbl(models.Model):
    user_key = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=20)
    user_pwd = models.TextField()
    name = models.TextField()
    tot_income = models.IntegerField()
    income = models.IntegerField()
    grade = models.CharField(max_length=2)
    favor = models.TextField()
    email = models.CharField(max_length=60)
    access_lv = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'member_tbl'


class NwpCommentmeta(models.Model):
    meta_id = models.BigIntegerField(primary_key=True)
    comment_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True)
    meta_value = models.TextField(blank=True)

    class Meta:
        # managed = False
        db_table = 'nwp_commentmeta'


class NwpComments(models.Model):
    comment_id = models.BigIntegerField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.BigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        # managed = False
        db_table = 'nwp_comments'


class NwpLinks(models.Model):
    link_id = models.BigIntegerField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.BigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        # managed = False
        db_table = 'nwp_links'


class NwpOptions(models.Model):
    option_id = models.BigIntegerField(primary_key=True)
    option_name = models.CharField(unique=True, max_length=64)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    class Meta:
        # managed = False
        db_table = 'nwp_options'


class NwpPostmeta(models.Model):
    meta_id = models.BigIntegerField(primary_key=True)
    post_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True)
    meta_value = models.TextField(blank=True)

    class Meta:
        # managed = False
        db_table = 'nwp_postmeta'


class NwpPosts(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.BigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=20)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.BigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        # managed = False
        db_table = 'nwp_posts'


class NwpTermRelationships(models.Model):
    object_id = models.BigIntegerField()
    term_taxonomy_id = models.BigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'nwp_term_relationships'


class NwpTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigIntegerField(primary_key=True)
    term_id = models.BigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.BigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        # managed = False
        db_table = 'nwp_term_taxonomy'


class NwpTerms(models.Model):
    term_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=200)
    term_group = models.BigIntegerField()

    class Meta:
        # managed = False
        db_table = 'nwp_terms'


class NwpUsermeta(models.Model):
    umeta_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True)
    meta_value = models.TextField(blank=True)

    class Meta:
        # managed = False
        db_table = 'nwp_usermeta'


class NwpUsers(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=64)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=60)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        # managed = False
        db_table = 'nwp_users'


class NwpWysijaCampaign(models.Model):
    campaign_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        # managed = False
        db_table = 'nwp_wysija_campaign'


class NwpWysijaCampaignList(models.Model):
    list_id = models.IntegerField()
    campaign_id = models.IntegerField()
    filter = models.TextField(blank=True)

    class Meta:
        # managed = False
        db_table = 'nwp_wysija_campaign_list'


class NwpWysijaEmail(models.Model):
    email_id = models.IntegerField(primary_key=True)
    campaign_id = models.IntegerField()
    subject = models.CharField(max_length=250)
    body = models.TextField(blank=True)
    created_at = models.IntegerField(blank=True, null=True)
    modified_at = models.IntegerField(blank=True, null=True)
    sent_at = models.IntegerField(blank=True, null=True)
    from_email = models.CharField(max_length=250, blank=True)
    from_name = models.CharField(max_length=250, blank=True)
    replyto_email = models.CharField(max_length=250, blank=True)
    replyto_name = models.CharField(max_length=250, blank=True)
    attachments = models.TextField(blank=True)
    status = models.IntegerField()
    type = models.IntegerField()
    number_sent = models.IntegerField()
    number_opened = models.IntegerField()
    number_clicked = models.IntegerField()
    number_unsub = models.IntegerField()
    number_bounce = models.IntegerField()
    number_forward = models.IntegerField()
    params = models.TextField(blank=True)
    wj_data = models.TextField(blank=True)
    wj_styles = models.TextField(blank=True)

    class Meta:
        # managed = False
        db_table = 'nwp_wysija_email'


class NwpWysijaEmailUserStat(models.Model):
    user_id = models.IntegerField()
    email_id = models.IntegerField()
    sent_at = models.IntegerField()
    opened_at = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'nwp_wysija_email_user_stat'


class NwpWysijaEmailUserUrl(models.Model):
    email_id = models.IntegerField()
    user_id = models.IntegerField()
    url_id = models.IntegerField()
    clicked_at = models.IntegerField(blank=True, null=True)
    number_clicked = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'nwp_wysija_email_user_url'


class NwpWysijaList(models.Model):
    list_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250, blank=True)
    namekey = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    unsub_mail_id = models.IntegerField()
    welcome_mail_id = models.IntegerField()
    is_enabled = models.IntegerField()
    is_public = models.IntegerField()
    created_at = models.IntegerField(blank=True, null=True)
    ordering = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'nwp_wysija_list'


class NwpWysijaQueue(models.Model):
    user_id = models.IntegerField()
    email_id = models.IntegerField()
    send_at = models.IntegerField()
    priority = models.IntegerField()
    number_try = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'nwp_wysija_queue'


class NwpWysijaUrl(models.Model):
    url_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250, blank=True)
    url = models.TextField(blank=True)

    class Meta:
        # managed = False
        db_table = 'nwp_wysija_url'


class NwpWysijaUrlMail(models.Model):
    email_id = models.IntegerField()
    url_id = models.IntegerField()
    unique_clicked = models.IntegerField()
    total_clicked = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'nwp_wysija_url_mail'


class NwpWysijaUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    wpuser_id = models.IntegerField()
    email = models.CharField(unique=True, max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    ip = models.CharField(max_length=100)
    keyuser = models.CharField(max_length=255)
    created_at = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'nwp_wysija_user'


class NwpWysijaUserField(models.Model):
    field_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250, blank=True)
    column_name = models.CharField(max_length=250)
    type = models.IntegerField(blank=True, null=True)
    values = models.TextField(blank=True)
    default = models.CharField(max_length=250)
    is_required = models.IntegerField()
    error_message = models.CharField(max_length=250)

    class Meta:
        # managed = False
        db_table = 'nwp_wysija_user_field'


class NwpWysijaUserHistory(models.Model):
    history_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    email_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=250)
    details = models.TextField(blank=True)
    executed_at = models.IntegerField(blank=True, null=True)
    executed_by = models.IntegerField(blank=True, null=True)
    source = models.TextField(blank=True)

    class Meta:
        # managed = False
        db_table = 'nwp_wysija_user_history'


class NwpWysijaUserList(models.Model):
    list_id = models.IntegerField()
    user_id = models.IntegerField()
    sub_date = models.IntegerField(blank=True, null=True)
    unsub_date = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'nwp_wysija_user_list'


class ReserveTbl(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_key = models.IntegerField()
    title = models.TextField()
    address = models.TextField()
    request_time = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'reserve_tbl'


class UvCheck(models.Model):
    index = models.IntegerField(primary_key=True)
    ip = models.TextField()
    adw_key = models.IntegerField()
    in_time = models.IntegerField()
    out_time = models.IntegerField(blank=True, null=True)
    not_uv = models.IntegerField()
    count = models.IntegerField()
    survey_total = models.IntegerField()
    survey_good = models.IntegerField()
    survey_bad = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'uv_check'


class WithdrawRequestTbl(models.Model):
    index = models.IntegerField(primary_key=True)
    user_key = models.IntegerField()
    fb_id = models.TextField()
    name = models.TextField()
    current_income = models.IntegerField()
    request_amount = models.IntegerField()
    bank_name = models.TextField()
    account_no = models.TextField()
    account_holder = models.TextField()

    class Meta:
        # managed = False
        db_table = 'withdraw_request_tbl'


class DailyLog(models.Model):
    # id = models.IntegerField(primary_key=True)
    movie = models.ForeignKey("AdTbl", related_name="movie", verbose_name=u"영화")
    date = models.DateTimeField(default=timezone.now)
    ad_hit = models.PositiveIntegerField(default=0)
    uv_hit = models.PositiveIntegerField(default=0)
    post_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = u"일단위로그"
        verbose_name_plural = u"일단위로그"