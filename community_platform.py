class CommunityPlatform:
    def __init__(self):
        self.communities = []

    def add_community(self, community_name):
        self.communities.append(community_name)

    def remove_community(self, community_name):
        self.communities.remove(community_name)

class User:
    def __init__(self, name):
        self.name = name
        self.subscribed_communities = []

    def subscribe_to_community(self, community_name, platform):
        if community_name not in platform.communities:
            raise ValueError(f"Community '{community_name}' does not exist.")
        self.subscribed_communities.append(community_name)

    def unsubscribe_from_community(self, community_name, platform):
        if community_name in platform.communities:
            self.subscribed_communities.remove(community_name)

    def is_subscribed_to(self, community_name):
        return community_name in self.subscribed_communities
