import requests

base = "https://canary.discord.com/api/v10"

def fetch_applications(headers):
    uri = f"{base}/applications"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applications_id(headers, application_id):
    uri = f"{base}/applications/{application_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applications_id_branches(headers, application_id):
    uri = f"{base}/applications/{application_id}/branches"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applications_id_branches_id_builds(headers, application_id, branch_id):
    uri = f"{base}/applications/{application_id}/branches/{branch_id}/builds"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applications_id_branches_id_builds_id(headers, application_id, branch_id, build_id):
    uri = f"{base}/applications/{application_id}/branches/{branch_id}/builds/{build_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applications_id_branches_id_builds_live(headers, application_id, branch_id, locale, platform):
    uri = f"{base}/applications/{application_id}/branches/{branch_id}/builds/live?locale={locale}&platform={platform}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applications_id_commands(headers, application_id):
    uri = f"{base}/applications/{application_id}/commands"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applications_id_commands_id(headers, application_id, command_id):
    uri = f"{base}/applications/{application_id}/commands/{command_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applications_id_guilds_id_commands_permissions(headers, application_id, guild_id):
    uri = f"{base}/applications/{application_id}/guilds/{guild_id}/commands/permissions"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applications_id_skus(headers, application_id):
    uri = f"{base}/applications/{application_id}/skus"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applications_id_public(headers, application_id):
    uri = f"{base}/applications/{application_id}/public"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applications_detectable(headers):
    uri = f"{base}/applications/detectable"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applicationdirectory_applications_id(headers, application_id):
    uri = f"{base}/application-directory/applications/{application_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applicationdirectory_applications_id_similar(headers, application_id):
    uri = f"{base}/application-directory/applications/{application_id}/similar"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applicationdirectory_applications_recommended(headers):
    uri = f"{base}/application-directory/applications/recommended"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applicationdirectory_categories(headers):
    uri = f"{base}/application-directory/categories"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applicationdirectory_collections(headers):
    uri = f"{base}/application-directory/collections"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applicationdirectory_search(headers):
    uri = f"{base}/application-directory/search"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applicationnews(headers):
    uri = f"{base}/application-news"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_applicationnews_id(headers, news_id):
    uri = f"{base}/application-news/{news_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_activities(headers):
    uri = f"{base}/activities"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_activities_statistics_applications_id(headers, application_id):
    uri = f"{base}/activities/statistics/applications/{application_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_auth_locationmetadata(headers):
    uri = f"{base}/auth/location-metadata"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_auth_login(headers):
    uri = f"{base}/auth/login"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_auth_register(headers):
    uri = f"{base}/auth/register"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_auth_sessions(headers):
    uri = f"{base}/auth/sessions"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id(headers, channel_id):
    uri = f"{base}/channels/{channel_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_call(headers, channel_id):
    uri = f"{base}/channels/{channel_id}/call"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_followerstats(headers, channel_id):
    uri = f"{base}/channels/{channel_id}/follower-stats"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_followermessagestats(headers, channel_id):
    uri = f"{base}/channels/{channel_id}/follower-message-stats"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_invites(headers, channel_id):
    uri = f"{base}/channels/{channel_id}/invites"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_messages(headers, channel_id, limit=50, before=None):
    uri = f"{base}/channels/{channel_id}/messages?limit={limit}"
    if before:
        uri += f"&before={before}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_messages_search(headers, channel_id):
    uri = f"{base}/channels/{channel_id}/messages/search"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_messages_id(headers, channel_id, message_id):
    uri = f"{base}/channels/{channel_id}/messages/{message_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_messages_id_reactions_id(headers, channel_id, message_id, emoji_id):
    uri = f"{base}/channels/{channel_id}/messages/{message_id}/reactions/{emoji_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_pins(headers, channel_id):
    uri = f"{base}/channels/{channel_id}/pins"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_storelisting(headers, channel_id):
    uri = f"{base}/channels/{channel_id}/store-listing"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_storelisting_id(headers, channel_id, sku_id):
    uri = f"{base}/channels/{channel_id}/store-listing/{sku_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_users_me_threads_archived_private(headers, channel_id):
    uri = f"{base}/channels/{channel_id}/users/@me/threads/archived/private"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_webhooks(headers, channel_id):
    uri = f"{base}/channels/{channel_id}/webhooks"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_thread_members(headers, channel_id):
    uri = f"{base}/channels/{channel_id}/thread-members"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_threads_active(headers, channel_id):
    uri = f"{base}/channels/{channel_id}/threads/active"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_threads_archived_private(headers, channel_id):
    uri = f"{base}/channels/{channel_id}/threads/archived/private"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_threads_archived_public(headers, channel_id):
    uri = f"{base}/channels/{channel_id}/threads/archived/public"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_channels_id_threads_search(headers, channel_id):
    uri = f"{base}/channels/{channel_id}/threads/search"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_connections_id_authorize(headers, provider_id):
    uri = f"{base}/connections/{provider_id}/authorize"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_discoverableguilds(headers):
    uri = f"{base}/discoverable-guilds"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_discovery_categories(headers):
    uri = f"{base}/discovery/categories"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_discovery_validterm(headers, term):
    uri = f"{base}/discovery/valid-term?term={term}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_entitlements_giftcodes_id(headers, gift_code):
    uri = f"{base}/entitlements/gift-codes/{gift_code}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_experiments(headers):
    uri = f"{base}/experiments"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_experiments_withguildexperiments(headers):
    uri = f"{base}/experiments?with_guild_experiments=true"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_friendsuggestions(headers):
    uri = f"{base}/friend-suggestions"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_gateway(headers):
    uri = f"{base}/gateway"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_gateway_bot(headers):
    uri = f"{base}/gateway/bot"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_gifs_suggest(headers, q):
    uri = f"{base}/gifs/suggest?q={q}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_gifs_trending(headers):
    uri = f"{base}/gifs/trending"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_gifs_trendingsearch(headers):
    uri = f"{base}/gifs/trending-search"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_activechannels(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/active-channels"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_adminservereligibility(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/admin-server-eligibility"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_analytics_memberinsights(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/analytics/member-insights"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_analytics_overview(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/analytics/overview"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_analytics_engagement_overview(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/analytics/engagement/overview"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_analytics_growthactivation_overview(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/analytics/growth-activation/overview"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_analytics_growthactivation_retention(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/analytics/growth-activation/retention"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_applications(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/applications"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_auditlogs(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/audit-logs"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_bans(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/bans"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_bans_id(headers, guild_id, user_id):
    uri = f"{base}/guilds/{guild_id}/bans/{user_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_channels(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/channels"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_connectionsconfigurations(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/connections-configurations"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_discoverymetadata(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/discovery-metadata"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_discoveryrequirements(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/discovery-requirements"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_emojis(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/emojis"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_emojis_id(headers, guild_id, emoji_id):
    uri = f"{base}/guilds/{guild_id}/emojis/{emoji_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_entitlements(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/entitlements"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_integrations(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/integrations"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_invites(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/invites"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_members(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/members"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_members_id(headers, guild_id, user_id):
    uri = f"{base}/guilds/{guild_id}/members/{user_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_membersverification(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/members-verification"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_messages_search(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/messages/search"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_premium_subscriptions(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/premium/subscriptions"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_preview(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/preview"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_prune(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/prune"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_regions(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/regions"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_requests(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/requests"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_roles(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/roles"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_roles_id_memberids(headers, guild_id, role_id):
    uri = f"{base}/guilds/{guild_id}/roles/{role_id}/member-ids"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_roles_id_connections_configurations(headers, guild_id, role_id):
    uri = f"{base}/guilds/{guild_id}/roles/{role_id}/connections-configurations"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_roles_id_connections_eligibility(headers, guild_id, role_id):
    uri = f"{base}/guilds/{guild_id}/roles/{role_id}/connections-eligibility"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_roles_membercounts(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/roles/member-counts"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_stickers(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/stickers"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_stickers_id(headers, guild_id, sticker_id):
    uri = f"{base}/guilds/{guild_id}/stickers/{sticker_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_templates(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/templates"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_topemojis(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/top-emojis"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_topreadchannels(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/top-read-channels"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_vanityurl(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/vanity-url"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_webhooks(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/webhooks"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_welcomescreen(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/welcome-screen"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_widget(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/widget"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_widget_json(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/widget.json"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_widget_png(headers, guild_id):
    uri = f"{base}/guilds/{guild_id}/widget.png"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_guilds_id_templates_id(headers, guild_id, template_id):
    uri = f"{base}/guilds/{guild_id}/templates/{template_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_invites_id(headers, invite_id):
    uri = f"{base}/invites/{invite_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_oauth2_me(headers):
    uri = f"{base}/oauth2/@me"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_oauth2_applications(headers):
    uri = f"{base}/oauth2/applications"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_oauth2_applications_id(headers, application_id):
    uri = f"{base}/oauth2/applications/{application_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_oauth2_applications_id_rpc(headers, application_id):
    uri = f"{base}/oauth2/applications/{application_id}/rpc"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_oauth2_applications_id_assets(headers, application_id):
    uri = f"{base}/oauth2/applications/{application_id}/assets"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_oauth2_authorize_client_id(headers, client_id):
    uri = f"{base}/oauth2/authorize?client_id={client_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_oauth2_authorize_webhookchannels_guild_id(headers, guild_id):
    uri = f"{base}/oauth2/authorize/webhook-channels?guild_id={guild_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_oauth2_samsung_authorize_client_id_redirect_uri_state(headers, client_id, redirect_uri, state):
    uri = f"{base}/oauth2/samsung/authorize?client_id={client_id}&redirect_uri={redirect_uri}&state={state}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_oauth2_tokens(headers):
    uri = f"{base}/oauth2/tokens"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_oauth2_tokens_id(headers, token_id):
    uri = f"{base}/oauth2/tokens/{token_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_outboundpromotions(headers):
    uri = f"{base}/outbound-promotions"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_partners_connections(headers):
    uri = f"{base}/partners/connections"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_partners_id_requirements(headers, guild_id):
    uri = f"{base}/partners/{guild_id}/requirements"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_reporting_menu_name2id(headers, name2):
    uri = f"{base}/reporting/menu/{name2}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_stageinstances_channel_id(headers, channel_id):
    uri = f"{base}/stage-instances/{channel_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_stageinstances_extra(headers):
    uri = f"{base}/stage-instances/extra"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_stickerpacks(headers):
    uri = f"{base}/sticker-packs"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_stickerpacks_id(headers, sticker_pack_id):
    uri = f"{base}/sticker-packs/{sticker_pack_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_stickerpacks_directoryv2_id(headers, store_directory_layout_id):
    uri = f"{base}/sticker-packs/directory/v2/{store_directory_layout_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_stickers_id_guild(headers, sticker_id):
    uri = f"{base}/stickers/{sticker_id}/guild"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_store_pricetiers(headers):
    uri = f"{base}/store/price-tiers"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_store_publishedlistings_applications_id(headers, application_id):
    uri = f"{base}/store/published-listings/applications/{application_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_store_publishedlistings_skus_id(headers, application_id):
    uri = f"{base}/store/published-listings/skus/{application_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_store_skus_id(headers, application_id):
    uri = f"{base}/store/skus/{application_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_store_skus_id_listings(headers, application_id):
    uri = f"{base}/store/skus/{application_id}/listings"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_streams_id_preview(headers, stream_key):
    uri = f"{base}/streams/{stream_key}/preview"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_teams(headers):
    uri = f"{base}/teams"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_id(headers, user_id):
    uri = f"{base}/users/{user_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_id_channels(headers, user_id):
    uri = f"{base}/users/{user_id}/channels"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_id_profile(headers, user_id):
    uri = f"{base}/users/{user_id}/profile"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_id_relationships(headers, user_id):
    uri = f"{base}/users/{user_id}/relationships"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_id_sessions_id_activities_id_metadata(headers, user_id, session_id, application_id):
    uri = f"{base}/users/{user_id}/sessions/{session_id}/activities/{application_id}/metadata"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me(headers):
    uri = f"{base}/users/@me"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_withanalyticstoken(headers):
    uri = f"{base}/users/@me?with_analytics_token=true"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_activities_statistics_applications(headers):
    uri = f"{base}/users/@me/activities/statistics/applications"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_affinities_users(headers):
    uri = f"{base}/users/@me/affinities/users"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_applications_id_achievements(headers, application_id):
    uri = f"{base}/users/@me/applications/{application_id}/achievements"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_applications_id_entitlements(headers, application_id):
    uri = f"{base}/users/@me/applications/{application_id}/entitlements"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_applications_roleconnections(headers):
    uri = f"{base}/users/@me/applications/role-connections"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_billing_countrycode(headers):
    uri = f"{base}/users/@me/billing/country-code"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_eligibleapplicationsubscriptionguilds_application_id(headers, application_id):
    uri = f"{base}/users/@me/eligible-application-subscription-guilds?application_id={application_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_billing_localizedpricingpromo(headers):
    uri = f"{base}/users/@me/billing/localized-pricing-promo"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_billing_payments(headers):
    uri = f"{base}/users/@me/billing/payments"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_billing_paymentsources(headers):
    uri = f"{base}/users/@me/billing/payment-sources"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_billing_paymentsources_id(headers, payment_source):
    uri = f"{base}/users/@me/billing/payment-sources/{payment_source}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_billing_stripe_paymentintents_payments_id(headers, payment_id):
    uri = f"{base}/users/@me/billing/stripe/payment-intents/payments/{payment_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_billing_subscriptions(headers):
    uri = f"{base}/users/@me/billing/subscriptions"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_billing_subscriptions_id(headers, subscription_id):
    uri = f"{base}/users/@me/billing/subscriptions/{subscription_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_channels(headers):
    uri = f"{base}/users/@me/channels"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_connections(headers):
    uri = f"{base}/users/@me/connections"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_connections_contacts_me_externalfriendlistentries_settings(headers):
    uri = f"{base}/users/@me/connections/contacts/@me/external-friend-list-entries/settings"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_consent(headers):
    uri = f"{base}/users/@me/consent"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_devices_synctoken(headers):
    uri = f"{base}/users/@me/devices/sync-token"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_emailsettings(headers):
    uri = f"{base}/users/@me/email-settings"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_etitlements(headers):
    uri = f"{base}/users/@me/etitlements"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_entitlements_gifts(headers):
    uri = f"{base}/users/@me/entitlements/gifts"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_feed_settings(headers):
    uri = f"{base}/users/@me/feed/settings"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_guilds(headers):
    uri = f"{base}/users/@me/guilds"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_guilds_premium_subscriptions(headers):
    uri = f"{base}/users/@me/guilds/premium/subscriptions"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_guilds_premium_subscriptionslots(headers):
    uri = f"{base}/users/@me/guilds/premium/subscription-slots"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_guilds_premium_subscription_cooldown(headers):
    uri = f"{base}/users/@me/guilds/premium/subscription/cooldown"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_harvest(headers):
    uri = f"{base}/users/@me/harvest"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_invites(headers):
    uri = f"{base}/users/@me/invites"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_joinrequestguilds(headers):
    uri = f"{base}/users/@me/join-request-guilds"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_library(headers):
    uri = f"{base}/users/@me/library"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_mentions(headers):
    uri = f"{base}/users/@me/mentions"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_mfa_webauthn_credentials(headers):
    uri = f"{base}/users/@me/mfa/webauthn/credentials"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_notes(headers):
    uri = f"{base}/users/@me/notes"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_notes_id(headers, note_user_id):
    uri = f"{base}/users/@me/notes/{note_user_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_outboundpromotions_codes(headers):
    uri = f"{base}/users/@me/outbound-promotions/codes"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_premiumusage(headers):
    uri = f"{base}/users/@me/premium-usage"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_relationships(headers):
    uri = f"{base}/users/@me/relationships"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_settings(headers):
    uri = f"{base}/users/@me/settings"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_settingsproto_type(headers, type):
    uri = f"{base}/users/@me/settings-proto/{type}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_users_me_messagerequests_supplementaldata_channel_ids(headers, channel_ids):
    uri = f"{base}/users/@me/message-requests/supplemental-data?channel_ids={channel_ids}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_voice_regions(headers):
    uri = f"{base}/voice/regions"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_voice_ice(headers):
    uri = f"{base}/voice/ice"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_webhooks_id_interaction_token_messages_original(headers, application_id, interaction_token):
    uri = f"{base}/webhooks/{application_id}/{interaction_token}/messages/@original"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_webhooks_id(headers, webhook_id):
    uri = f"{base}/webhooks/{webhook_id}"
    r = requests.get(uri, headers=headers)
    return r.json()

def fetch_webhooks_id_token(headers, webhook_id, webhook_token):
    uri = f"{base}/webhooks/{webhook_id}/{webhook_token}"
    r = requests.get(uri, headers=headers)
    return r.json()