from django.contrib.auth.models import User
from rest_framework import serializers
from backend.models import Nickname, Quote, LeaderbordPosition

class UserSerializer(serializers.HyperlinkedModelSerializer):
  nickname = serializers.StringRelatedField(read_only=True)
  mongolen_board_position = serializers.StringRelatedField(read_only=True)

  class Meta:
    model = User
    fields = [
      'url',
      'username',
      'first_name',
      'last_name',
      'email',
      'date_joined',
      'nickname',
      'mongolen_board_position'
    ]

class NicknameSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Nickname
    fields = [
      'url',
      'user',
      'nickname'
    ]

class QuoteSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Quote
    fields = [
      'url',
      'user',
      'quote',
      'date'
    ]

class LeaderboardPositionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = LeaderbordPosition
    fields = [
      'url',
      'user',
      'position'
    ]