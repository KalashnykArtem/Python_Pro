from abc import ABC, abstractmethod
from datetime import datetime
from time import sleep


class SocialChannel(ABC):
    @abstractmethod
    def type_channel(self):
        """Represents the type of channel"""

    @abstractmethod
    def number_followers(self):
        """Represents the number of channel followers"""

    @abstractmethod
    def post_a_message(self, message: str):
        """Post a message to a social channel"""


class Youtube(SocialChannel):
    def __init__(self, number_followers: int):
        self.number_followers = number_followers

    @property
    def type_channel(self):
        return "Youtube"

    def number_followers(self):
        return getattr(self, "_number_followers")

    def post_a_message(self, message: str):
        print(f"{message} posted on {self.type_channel} at {datetime.now()}")

    def __str__(self):
        return f"{self.type_channel}: {self.number_followers} followers"


class Facebook(SocialChannel):
    def __init__(self, number_followers: int):
        self.number_followers = number_followers

    @property
    def type_channel(self):
        return "Facebook"

    def number_followers(self):
        return getattr(self, "_number_followers")

    def post_a_message(self, message: str):
        print(f"{message} posted on {self.type_channel} at {datetime.now()}")

    def __str__(self):
        return f"{self.type_channel}: {self.number_followers} followers"


class Twitter(SocialChannel):
    def __init__(self, number_followers: int):
        self.number_followers = number_followers

    @property
    def type_channel(self):
        return "Twitter"

    def number_followers(self):
        return getattr(self, "_number_followers")

    def post_a_message(self, message: str):
        print(f"{message} posted on {self.type_channel} at {datetime.now()}")

    def __str__(self):
        return f"{self.type_channel}: {self.number_followers} followers"


class Post:
    def __init__(self, message: str, timestamp: int):
        self.message = message
        self.timestamp = timestamp


def time_dispatch(current_time: datetime, seconds: int):
    time_dispatch = current_time.timestamp() + seconds
    return datetime.fromtimestamp(time_dispatch)


def process_schedule(posts: list[Post], channels: list[SocialChannel]):
    for post in posts:
        if post.timestamp >= datetime.now():
            sleep(post.timestamp.timestamp() - datetime.now().timestamp())
            for channel in channels:
                channel.post_a_message(post.message)


def main():
    current_time = datetime.now()
    posts = [
        Post("Hello #1", time_dispatch(current_time, 5)),
        Post("Hello #2", time_dispatch(current_time, 15)),
    ]

    channels = [Youtube(1_000_000), Facebook(10_000_000), Twitter(5_000_000)]

    for channel in channels:
        print(channel)

    process_schedule(posts, channels)


if __name__ == "__main__":
    main()
