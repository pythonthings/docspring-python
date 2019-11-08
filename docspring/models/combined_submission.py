# coding: utf-8

"""
    API v1

    DocSpring is a service that helps you fill out and sign PDF templates.  # noqa: E501

    OpenAPI spec version: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CombinedSubmission(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'metadata': 'object',
        'expired': 'bool',
        'expires_at': 'str',
        'source_pdfs': 'list[object]',
        'download_url': 'str',
        'submission_ids': 'list[str]',
        'id': 'str',
        'state': 'str',
        'actions': 'list[CombinedSubmissionAction]'
    }

    attribute_map = {
        'metadata': 'metadata',
        'expired': 'expired',
        'expires_at': 'expires_at',
        'source_pdfs': 'source_pdfs',
        'download_url': 'download_url',
        'submission_ids': 'submission_ids',
        'id': 'id',
        'state': 'state',
        'actions': 'actions'
    }

    def __init__(self, metadata=None, expired=None, expires_at=None, source_pdfs=None, download_url=None, submission_ids=None, id=None, state=None, actions=None):  # noqa: E501
        """CombinedSubmission - a model defined in OpenAPI"""  # noqa: E501

        self._metadata = None
        self._expired = None
        self._expires_at = None
        self._source_pdfs = None
        self._download_url = None
        self._submission_ids = None
        self._id = None
        self._state = None
        self._actions = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if expired is not None:
            self.expired = expired
        if expires_at is not None:
            self.expires_at = expires_at
        if source_pdfs is not None:
            self.source_pdfs = source_pdfs
        if download_url is not None:
            self.download_url = download_url
        if submission_ids is not None:
            self.submission_ids = submission_ids
        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if actions is not None:
            self.actions = actions

    @property
    def metadata(self):
        """Gets the metadata of this CombinedSubmission.  # noqa: E501


        :return: The metadata of this CombinedSubmission.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CombinedSubmission.


        :param metadata: The metadata of this CombinedSubmission.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def expired(self):
        """Gets the expired of this CombinedSubmission.  # noqa: E501


        :return: The expired of this CombinedSubmission.  # noqa: E501
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this CombinedSubmission.


        :param expired: The expired of this CombinedSubmission.  # noqa: E501
        :type: bool
        """

        self._expired = expired

    @property
    def expires_at(self):
        """Gets the expires_at of this CombinedSubmission.  # noqa: E501


        :return: The expires_at of this CombinedSubmission.  # noqa: E501
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this CombinedSubmission.


        :param expires_at: The expires_at of this CombinedSubmission.  # noqa: E501
        :type: str
        """

        self._expires_at = expires_at

    @property
    def source_pdfs(self):
        """Gets the source_pdfs of this CombinedSubmission.  # noqa: E501


        :return: The source_pdfs of this CombinedSubmission.  # noqa: E501
        :rtype: list[object]
        """
        return self._source_pdfs

    @source_pdfs.setter
    def source_pdfs(self, source_pdfs):
        """Sets the source_pdfs of this CombinedSubmission.


        :param source_pdfs: The source_pdfs of this CombinedSubmission.  # noqa: E501
        :type: list[object]
        """

        self._source_pdfs = source_pdfs

    @property
    def download_url(self):
        """Gets the download_url of this CombinedSubmission.  # noqa: E501


        :return: The download_url of this CombinedSubmission.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this CombinedSubmission.


        :param download_url: The download_url of this CombinedSubmission.  # noqa: E501
        :type: str
        """

        self._download_url = download_url

    @property
    def submission_ids(self):
        """Gets the submission_ids of this CombinedSubmission.  # noqa: E501


        :return: The submission_ids of this CombinedSubmission.  # noqa: E501
        :rtype: list[str]
        """
        return self._submission_ids

    @submission_ids.setter
    def submission_ids(self, submission_ids):
        """Sets the submission_ids of this CombinedSubmission.


        :param submission_ids: The submission_ids of this CombinedSubmission.  # noqa: E501
        :type: list[str]
        """

        self._submission_ids = submission_ids

    @property
    def id(self):
        """Gets the id of this CombinedSubmission.  # noqa: E501


        :return: The id of this CombinedSubmission.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CombinedSubmission.


        :param id: The id of this CombinedSubmission.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this CombinedSubmission.  # noqa: E501


        :return: The state of this CombinedSubmission.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CombinedSubmission.


        :param state: The state of this CombinedSubmission.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "processed", "error"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def actions(self):
        """Gets the actions of this CombinedSubmission.  # noqa: E501


        :return: The actions of this CombinedSubmission.  # noqa: E501
        :rtype: list[CombinedSubmissionAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this CombinedSubmission.


        :param actions: The actions of this CombinedSubmission.  # noqa: E501
        :type: list[CombinedSubmissionAction]
        """

        self._actions = actions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CombinedSubmission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other