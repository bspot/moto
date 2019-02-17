from __future__ import unicode_literals

from moto.core.responses import BaseResponse
from .models import iam_backend, User


class IamResponse(BaseResponse):

    def attach_role_policy(self):
        policy_arn = self._get_param('PolicyArn')
        role_name = self._get_param('RoleName')
        iam_backend.attach_role_policy(policy_arn, role_name)
        template = self.response_template(ATTACH_ROLE_POLICY_TEMPLATE)
        return template.render()

    def detach_role_policy(self):
        role_name = self._get_param('RoleName')
        policy_arn = self._get_param('PolicyArn')
        iam_backend.detach_role_policy(policy_arn, role_name)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name="DetachRolePolicyResponse")

    def attach_group_policy(self):
        policy_arn = self._get_param('PolicyArn')
        group_name = self._get_param('GroupName')
        iam_backend.attach_group_policy(policy_arn, group_name)
        template = self.response_template(ATTACH_GROUP_POLICY_TEMPLATE)
        return template.render()

    def detach_group_policy(self):
        policy_arn = self._get_param('PolicyArn')
        group_name = self._get_param('GroupName')
        iam_backend.detach_group_policy(policy_arn, group_name)
        template = self.response_template(DETACH_GROUP_POLICY_TEMPLATE)
        return template.render()

    def attach_user_policy(self):
        policy_arn = self._get_param('PolicyArn')
        user_name = self._get_param('UserName')
        iam_backend.attach_user_policy(policy_arn, user_name)
        template = self.response_template(ATTACH_USER_POLICY_TEMPLATE)
        return template.render()

    def detach_user_policy(self):
        policy_arn = self._get_param('PolicyArn')
        user_name = self._get_param('UserName')
        iam_backend.detach_user_policy(policy_arn, user_name)
        template = self.response_template(DETACH_USER_POLICY_TEMPLATE)
        return template.render()

    def create_policy(self):
        description = self._get_param('Description')
        path = self._get_param('Path')
        policy_document = self._get_param('PolicyDocument')
        policy_name = self._get_param('PolicyName')
        policy = iam_backend.create_policy(
            description, path, policy_document, policy_name)
        template = self.response_template(CREATE_POLICY_TEMPLATE)
        return template.render(policy=policy)

    def get_policy(self):
        policy_arn = self._get_param('PolicyArn')
        policy = iam_backend.get_policy(policy_arn)
        template = self.response_template(GET_POLICY_TEMPLATE)
        return template.render(policy=policy)

    def list_attached_role_policies(self):
        marker = self._get_param('Marker')
        max_items = self._get_int_param('MaxItems', 100)
        path_prefix = self._get_param('PathPrefix', '/')
        role_name = self._get_param('RoleName')
        policies, marker = iam_backend.list_attached_role_policies(
            role_name, marker=marker, max_items=max_items, path_prefix=path_prefix)
        template = self.response_template(LIST_ATTACHED_ROLE_POLICIES_TEMPLATE)
        return template.render(policies=policies, marker=marker)

    def list_attached_group_policies(self):
        marker = self._get_param('Marker')
        max_items = self._get_int_param('MaxItems', 100)
        path_prefix = self._get_param('PathPrefix', '/')
        group_name = self._get_param('GroupName')
        policies, marker = iam_backend.list_attached_group_policies(
            group_name, marker=marker, max_items=max_items,
            path_prefix=path_prefix)
        template = self.response_template(LIST_ATTACHED_GROUP_POLICIES_TEMPLATE)
        return template.render(policies=policies, marker=marker)

    def list_attached_user_policies(self):
        marker = self._get_param('Marker')
        max_items = self._get_int_param('MaxItems', 100)
        path_prefix = self._get_param('PathPrefix', '/')
        user_name = self._get_param('UserName')
        policies, marker = iam_backend.list_attached_user_policies(
            user_name, marker=marker, max_items=max_items,
            path_prefix=path_prefix)
        template = self.response_template(LIST_ATTACHED_USER_POLICIES_TEMPLATE)
        return template.render(policies=policies, marker=marker)

    def list_policies(self):
        marker = self._get_param('Marker')
        max_items = self._get_int_param('MaxItems', 100)
        only_attached = self._get_bool_param('OnlyAttached', False)
        path_prefix = self._get_param('PathPrefix', '/')
        scope = self._get_param('Scope', 'All')
        policies, marker = iam_backend.list_policies(
            marker, max_items, only_attached, path_prefix, scope)
        template = self.response_template(LIST_POLICIES_TEMPLATE)
        return template.render(policies=policies, marker=marker)

    def list_entities_for_policy(self):
        template = self.response_template(LIST_ENTITIES_FOR_POLICY_TEMPLATE)
        return template.render()

    def create_role(self):
        role_name = self._get_param('RoleName')
        path = self._get_param('Path')
        assume_role_policy_document = self._get_param(
            'AssumeRolePolicyDocument')

        role = iam_backend.create_role(
            role_name, assume_role_policy_document, path)
        template = self.response_template(CREATE_ROLE_TEMPLATE)
        return template.render(role=role)

    def get_role(self):
        role_name = self._get_param('RoleName')
        role = iam_backend.get_role(role_name)

        template = self.response_template(GET_ROLE_TEMPLATE)
        return template.render(role=role)

    def delete_role(self):
        role_name = self._get_param('RoleName')
        iam_backend.delete_role(role_name)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name="DeleteRoleResponse")

    def list_role_policies(self):
        role_name = self._get_param('RoleName')
        role_policies_names = iam_backend.list_role_policies(role_name)
        template = self.response_template(LIST_ROLE_POLICIES)
        return template.render(role_policies=role_policies_names)

    def put_role_policy(self):
        role_name = self._get_param('RoleName')
        policy_name = self._get_param('PolicyName')
        policy_document = self._get_param('PolicyDocument')
        iam_backend.put_role_policy(role_name, policy_name, policy_document)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name="PutRolePolicyResponse")

    def delete_role_policy(self):
        role_name = self._get_param('RoleName')
        policy_name = self._get_param('PolicyName')
        iam_backend.delete_role_policy(role_name, policy_name)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name="DeleteRolePolicyResponse")

    def get_role_policy(self):
        role_name = self._get_param('RoleName')
        policy_name = self._get_param('PolicyName')
        policy_name, policy_document = iam_backend.get_role_policy(
            role_name, policy_name)
        template = self.response_template(GET_ROLE_POLICY_TEMPLATE)
        return template.render(role_name=role_name,
                               policy_name=policy_name,
                               policy_document=policy_document)

    def update_assume_role_policy(self):
        role_name = self._get_param('RoleName')
        role = iam_backend.get_role(role_name)
        role.assume_role_policy_document = self._get_param('PolicyDocument')
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name="UpdateAssumeRolePolicyResponse")

    def update_role_description(self):
        role_name = self._get_param('RoleName')
        description = self._get_param('Description')
        role = iam_backend.update_role_description(role_name,description)
        template = self.response_template(UPDATE_ROLE_DESCRIPTION_TEMPLATE)
        return template.render(role=role)

    def update_role(self):
        role_name = self._get_param('RoleName')
        description = self._get_param('Description')
        role = iam_backend.update_role_description(role_name,description)
        template = self.response_template(UPDATE_ROLE_DESCRIPTION_TEMPLATE)
        return template.render(role=role)

    def create_policy_version(self):
        policy_arn = self._get_param('PolicyArn')
        policy_document = self._get_param('PolicyDocument')
        set_as_default = self._get_param('SetAsDefault')
        policy_version = iam_backend.create_policy_version(policy_arn, policy_document, set_as_default)
        template = self.response_template(CREATE_POLICY_VERSION_TEMPLATE)
        return template.render(policy_version=policy_version)

    def get_policy_version(self):
        policy_arn = self._get_param('PolicyArn')
        version_id = self._get_param('VersionId')
        policy_version = iam_backend.get_policy_version(policy_arn, version_id)
        template = self.response_template(GET_POLICY_VERSION_TEMPLATE)
        return template.render(policy_version=policy_version)

    def list_policy_versions(self):
        policy_arn = self._get_param('PolicyArn')
        policy_versions = iam_backend.list_policy_versions(policy_arn)

        template = self.response_template(LIST_POLICY_VERSIONS_TEMPLATE)
        return template.render(policy_versions=policy_versions)

    def delete_policy_version(self):
        policy_arn = self._get_param('PolicyArn')
        version_id = self._get_param('VersionId')

        iam_backend.delete_policy_version(policy_arn, version_id)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name='DeletePolicyVersion')

    def create_instance_profile(self):
        profile_name = self._get_param('InstanceProfileName')
        path = self._get_param('Path', '/')

        profile = iam_backend.create_instance_profile(
            profile_name, path, role_ids=[])
        template = self.response_template(CREATE_INSTANCE_PROFILE_TEMPLATE)
        return template.render(profile=profile)

    def get_instance_profile(self):
        profile_name = self._get_param('InstanceProfileName')
        profile = iam_backend.get_instance_profile(profile_name)

        template = self.response_template(GET_INSTANCE_PROFILE_TEMPLATE)
        return template.render(profile=profile)

    def add_role_to_instance_profile(self):
        profile_name = self._get_param('InstanceProfileName')
        role_name = self._get_param('RoleName')

        iam_backend.add_role_to_instance_profile(profile_name, role_name)
        template = self.response_template(
            ADD_ROLE_TO_INSTANCE_PROFILE_TEMPLATE)
        return template.render()

    def remove_role_from_instance_profile(self):
        profile_name = self._get_param('InstanceProfileName')
        role_name = self._get_param('RoleName')

        iam_backend.remove_role_from_instance_profile(profile_name, role_name)
        template = self.response_template(
            REMOVE_ROLE_FROM_INSTANCE_PROFILE_TEMPLATE)
        return template.render()

    def list_roles(self):
        roles = iam_backend.get_roles()

        template = self.response_template(LIST_ROLES_TEMPLATE)
        return template.render(roles=roles)

    def list_instance_profiles(self):
        profiles = iam_backend.get_instance_profiles()

        template = self.response_template(LIST_INSTANCE_PROFILES_TEMPLATE)
        return template.render(instance_profiles=profiles)

    def list_instance_profiles_for_role(self):
        role_name = self._get_param('RoleName')
        profiles = iam_backend.get_instance_profiles_for_role(
            role_name=role_name)

        template = self.response_template(
            LIST_INSTANCE_PROFILES_FOR_ROLE_TEMPLATE)
        return template.render(instance_profiles=profiles)

    def upload_server_certificate(self):
        cert_name = self._get_param('ServerCertificateName')
        cert_body = self._get_param('CertificateBody')
        path = self._get_param('Path')
        private_key = self._get_param('PrivateKey')
        cert_chain = self._get_param('CertificateName')

        cert = iam_backend.upload_server_cert(
            cert_name, cert_body, private_key, cert_chain=cert_chain, path=path)
        template = self.response_template(UPLOAD_CERT_TEMPLATE)
        return template.render(certificate=cert)

    def list_server_certificates(self, marker=None):
        certs = iam_backend.get_all_server_certs(marker=marker)
        template = self.response_template(LIST_SERVER_CERTIFICATES_TEMPLATE)
        return template.render(server_certificates=certs)

    def get_server_certificate(self):
        cert_name = self._get_param('ServerCertificateName')
        cert = iam_backend.get_server_certificate(cert_name)
        template = self.response_template(GET_SERVER_CERTIFICATE_TEMPLATE)
        return template.render(certificate=cert)

    def delete_server_certificate(self):
        cert_name = self._get_param('ServerCertificateName')
        iam_backend.delete_server_certificate(cert_name)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name="DeleteServerCertificate")

    def create_group(self):
        group_name = self._get_param('GroupName')
        path = self._get_param('Path', '/')

        group = iam_backend.create_group(group_name, path)
        template = self.response_template(CREATE_GROUP_TEMPLATE)
        return template.render(group=group)

    def get_group(self):
        group_name = self._get_param('GroupName')

        group = iam_backend.get_group(group_name)
        template = self.response_template(GET_GROUP_TEMPLATE)
        return template.render(group=group)

    def list_groups(self):
        groups = iam_backend.list_groups()
        template = self.response_template(LIST_GROUPS_TEMPLATE)
        return template.render(groups=groups)

    def list_groups_for_user(self):
        user_name = self._get_param('UserName')

        groups = iam_backend.get_groups_for_user(user_name)
        template = self.response_template(LIST_GROUPS_FOR_USER_TEMPLATE)
        return template.render(groups=groups)

    def put_group_policy(self):
        group_name = self._get_param('GroupName')
        policy_name = self._get_param('PolicyName')
        policy_document = self._get_param('PolicyDocument')
        iam_backend.put_group_policy(group_name, policy_name, policy_document)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name="PutGroupPolicyResponse")

    def list_group_policies(self):
        group_name = self._get_param('GroupName')
        marker = self._get_param('Marker')
        max_items = self._get_param('MaxItems')
        policies = iam_backend.list_group_policies(group_name,
            marker=marker, max_items=max_items)
        template = self.response_template(LIST_GROUP_POLICIES_TEMPLATE)
        return template.render(name="ListGroupPoliciesResponse",
                               policies=policies,
                               marker=marker)

    def get_group_policy(self):
        group_name = self._get_param('GroupName')
        policy_name = self._get_param('PolicyName')
        policy_result = iam_backend.get_group_policy(group_name, policy_name)
        template = self.response_template(GET_GROUP_POLICY_TEMPLATE)
        return template.render(name="GetGroupPolicyResponse", **policy_result)

    def create_user(self):
        user_name = self._get_param('UserName')
        path = self._get_param('Path')

        user = iam_backend.create_user(user_name, path)
        template = self.response_template(USER_TEMPLATE)
        return template.render(action='Create', user=user)

    def get_user(self):
        user_name = self._get_param('UserName')
        if user_name:
            user = iam_backend.get_user(user_name)
        else:
            user = User(name='default_user')
            # If no user is specific, IAM returns the current user

        template = self.response_template(USER_TEMPLATE)
        return template.render(action='Get', user=user)

    def list_users(self):
        path_prefix = self._get_param('PathPrefix')
        marker = self._get_param('Marker')
        max_items = self._get_param('MaxItems')
        users = iam_backend.list_users(path_prefix, marker, max_items)
        template = self.response_template(LIST_USERS_TEMPLATE)
        return template.render(action='List', users=users)

    def create_login_profile(self):
        user_name = self._get_param('UserName')
        password = self._get_param('Password')
        password = self._get_param('Password')
        user = iam_backend.create_login_profile(user_name, password)

        template = self.response_template(CREATE_LOGIN_PROFILE_TEMPLATE)
        return template.render(user=user)

    def get_login_profile(self):
        user_name = self._get_param('UserName')
        user = iam_backend.get_login_profile(user_name)

        template = self.response_template(GET_LOGIN_PROFILE_TEMPLATE)
        return template.render(user=user)

    def update_login_profile(self):
        user_name = self._get_param('UserName')
        password = self._get_param('Password')
        password_reset_required = self._get_param('PasswordResetRequired')
        user = iam_backend.update_login_profile(user_name, password, password_reset_required)

        template = self.response_template(UPDATE_LOGIN_PROFILE_TEMPLATE)
        return template.render(user=user)

    def add_user_to_group(self):
        group_name = self._get_param('GroupName')
        user_name = self._get_param('UserName')

        iam_backend.add_user_to_group(group_name, user_name)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name='AddUserToGroup')

    def remove_user_from_group(self):
        group_name = self._get_param('GroupName')
        user_name = self._get_param('UserName')

        iam_backend.remove_user_from_group(group_name, user_name)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name='RemoveUserFromGroup')

    def get_user_policy(self):
        user_name = self._get_param('UserName')
        policy_name = self._get_param('PolicyName')

        policy_document = iam_backend.get_user_policy(user_name, policy_name)
        template = self.response_template(GET_USER_POLICY_TEMPLATE)
        return template.render(
            user_name=user_name,
            policy_name=policy_name,
            policy_document=policy_document.get('policy_document')
        )

    def list_user_policies(self):
        user_name = self._get_param('UserName')
        policies = iam_backend.list_user_policies(user_name)
        template = self.response_template(LIST_USER_POLICIES_TEMPLATE)
        return template.render(policies=policies)

    def put_user_policy(self):
        user_name = self._get_param('UserName')
        policy_name = self._get_param('PolicyName')
        policy_document = self._get_param('PolicyDocument')

        iam_backend.put_user_policy(user_name, policy_name, policy_document)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name='PutUserPolicy')

    def delete_user_policy(self):
        user_name = self._get_param('UserName')
        policy_name = self._get_param('PolicyName')

        iam_backend.delete_user_policy(user_name, policy_name)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name='DeleteUserPolicy')

    def create_access_key(self):
        user_name = self._get_param('UserName')

        key = iam_backend.create_access_key(user_name)
        template = self.response_template(CREATE_ACCESS_KEY_TEMPLATE)
        return template.render(key=key)

    def update_access_key(self):
        user_name = self._get_param('UserName')
        access_key_id = self._get_param('AccessKeyId')
        status = self._get_param('Status')
        iam_backend.update_access_key(user_name, access_key_id, status)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name='UpdateAccessKey')

    def get_access_key_last_used(self):
        access_key_id = self._get_param('AccessKeyId')
        last_used_response = iam_backend.get_access_key_last_used(access_key_id)
        template = self.response_template(GET_ACCESS_KEY_LAST_USED_TEMPLATE)
        return template.render(user_name=last_used_response["user_name"], last_used=last_used_response["last_used"])

    def list_access_keys(self):
        user_name = self._get_param('UserName')
        keys = iam_backend.get_all_access_keys(user_name)
        template = self.response_template(LIST_ACCESS_KEYS_TEMPLATE)
        return template.render(user_name=user_name, keys=keys)

    def delete_access_key(self):
        user_name = self._get_param('UserName')
        access_key_id = self._get_param('AccessKeyId')

        iam_backend.delete_access_key(access_key_id, user_name)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name='DeleteAccessKey')

    def deactivate_mfa_device(self):
        user_name = self._get_param('UserName')
        serial_number = self._get_param('SerialNumber')

        iam_backend.deactivate_mfa_device(user_name, serial_number)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name='DeactivateMFADevice')

    def enable_mfa_device(self):
        user_name = self._get_param('UserName')
        serial_number = self._get_param('SerialNumber')
        authentication_code_1 = self._get_param('AuthenticationCode1')
        authentication_code_2 = self._get_param('AuthenticationCode2')

        iam_backend.enable_mfa_device(
            user_name,
            serial_number,
            authentication_code_1,
            authentication_code_2
        )
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name='EnableMFADevice')

    def list_mfa_devices(self):
        user_name = self._get_param('UserName')
        devices = iam_backend.list_mfa_devices(user_name)
        template = self.response_template(LIST_MFA_DEVICES_TEMPLATE)
        return template.render(user_name=user_name, devices=devices)

    def delete_user(self):
        user_name = self._get_param('UserName')
        iam_backend.delete_user(user_name)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name='DeleteUser')

    def delete_login_profile(self):
        user_name = self._get_param('UserName')
        iam_backend.delete_login_profile(user_name)
        template = self.response_template(GENERIC_EMPTY_TEMPLATE)
        return template.render(name='DeleteLoginProfile')

    def generate_credential_report(self):
        if iam_backend.report_generated():
            template = self.response_template(CREDENTIAL_REPORT_GENERATED)
        else:
            template = self.response_template(CREDENTIAL_REPORT_GENERATING)
        iam_backend.generate_report()
        return template.render()

    def get_credential_report(self):
        report = iam_backend.get_credential_report()
        template = self.response_template(CREDENTIAL_REPORT)
        return template.render(report=report)

    def list_account_aliases(self):
        aliases = iam_backend.list_account_aliases()
        template = self.response_template(LIST_ACCOUNT_ALIASES_TEMPLATE)
        return template.render(aliases=aliases)

    def create_account_alias(self):
        alias = self._get_param('AccountAlias')
        iam_backend.create_account_alias(alias)
        template = self.response_template(CREATE_ACCOUNT_ALIAS_TEMPLATE)
        return template.render()

    def delete_account_alias(self):
        alias = self._get_param('AccountAlias')
        iam_backend.delete_account_alias(alias)
        template = self.response_template(DELETE_ACCOUNT_ALIAS_TEMPLATE)
        return template.render()

    def get_account_authorization_details(self):
        filter_param = self._get_multi_param('Filter.member')
        account_details = iam_backend.get_account_authorization_details(filter_param)
        template = self.response_template(GET_ACCOUNT_AUTHORIZATION_DETAILS_TEMPLATE)
        return template.render(
            instance_profiles=account_details['instance_profiles'],
            policies=account_details['managed_policies'],
            users=account_details['users'],
            groups=account_details['groups'],
            roles=account_details['roles'],
            get_groups_for_user=iam_backend.get_groups_for_user
        )

    def create_saml_provider(self):
        saml_provider_name = self._get_param('Name')
        saml_metadata_document = self._get_param('SAMLMetadataDocument')
        saml_provider = iam_backend.create_saml_provider(saml_provider_name, saml_metadata_document)

        template = self.response_template(CREATE_SAML_PROVIDER_TEMPLATE)
        return template.render(saml_provider=saml_provider)

    def update_saml_provider(self):
        saml_provider_arn = self._get_param('SAMLProviderArn')
        saml_metadata_document = self._get_param('SAMLMetadataDocument')
        saml_provider = iam_backend.update_saml_provider(saml_provider_arn, saml_metadata_document)

        template = self.response_template(UPDATE_SAML_PROVIDER_TEMPLATE)
        return template.render(saml_provider=saml_provider)

    def delete_saml_provider(self):
        saml_provider_arn = self._get_param('SAMLProviderArn')
        iam_backend.delete_saml_provider(saml_provider_arn)

        template = self.response_template(DELETE_SAML_PROVIDER_TEMPLATE)
        return template.render()

    def list_saml_providers(self):
        saml_providers = iam_backend.list_saml_providers()

        template = self.response_template(LIST_SAML_PROVIDERS_TEMPLATE)
        return template.render(saml_providers=saml_providers)

    def get_saml_provider(self):
        saml_provider_arn = self._get_param('SAMLProviderArn')
        saml_provider = iam_backend.get_saml_provider(saml_provider_arn)

        template = self.response_template(GET_SAML_PROVIDER_TEMPLATE)
        return template.render(saml_provider=saml_provider)

    def upload_signing_certificate(self):
        user_name = self._get_param('UserName')
        cert_body = self._get_param('CertificateBody')

        cert = iam_backend.upload_signing_certificate(user_name, cert_body)
        template = self.response_template(UPLOAD_SIGNING_CERTIFICATE_TEMPLATE)
        return template.render(cert=cert)

    def update_signing_certificate(self):
        user_name = self._get_param('UserName')
        cert_id = self._get_param('CertificateId')
        status = self._get_param('Status')

        iam_backend.update_signing_certificate(user_name, cert_id, status)
        template = self.response_template(UPDATE_SIGNING_CERTIFICATE_TEMPLATE)
        return template.render()

    def delete_signing_certificate(self):
        user_name = self._get_param('UserName')
        cert_id = self._get_param('CertificateId')

        iam_backend.delete_signing_certificate(user_name, cert_id)
        template = self.response_template(DELETE_SIGNING_CERTIFICATE_TEMPLATE)
        return template.render()

    def list_signing_certificates(self):
        user_name = self._get_param('UserName')

        certs = iam_backend.list_signing_certificates(user_name)
        template = self.response_template(LIST_SIGNING_CERTIFICATES_TEMPLATE)
        return template.render(user_name=user_name, certificates=certs)

    def list_role_tags(self):
        role_name = self._get_param('RoleName')
        marker = self._get_param('Marker')
        max_items = self._get_param('MaxItems', 100)

        tags, marker = iam_backend.list_role_tags(role_name, marker, max_items)

        template = self.response_template(LIST_ROLE_TAG_TEMPLATE)
        return template.render(tags=tags, marker=marker)

    def tag_role(self):
        role_name = self._get_param('RoleName')
        tags = self._get_multi_param('Tags.member')

        iam_backend.tag_role(role_name, tags)

        template = self.response_template(TAG_ROLE_TEMPLATE)
        return template.render()

    def untag_role(self):
        role_name = self._get_param('RoleName')
        tag_keys = self._get_multi_param('TagKeys.member')

        iam_backend.untag_role(role_name, tag_keys)

        template = self.response_template(UNTAG_ROLE_TEMPLATE)
        return template.render()

LIST_ENTITIES_FOR_POLICY_TEMPLATE = """<ListEntitiesForPolicyResponse>
 <ListEntitiesForPolicyResult>
 <PolicyRoles>
 <member>
 <RoleName>DevRole</RoleName>
 </member>
 </PolicyRoles>
 <PolicyGroups>
 <member>
 <GroupName>Dev</GroupName>
 </member>
 </PolicyGroups>
 <IsTruncated>false</IsTruncated>
 <PolicyUsers>
 <member>
 <UserName>Alice</UserName>
 </member>
 <member>
 <UserName>Bob</UserName>
 </member>
 </PolicyUsers>
 </ListEntitiesForPolicyResult>
 <ResponseMetadata>
 <RequestId>eb358e22-9d1f-11e4-93eb-190ecEXAMPLE</RequestId>
 </ResponseMetadata>
</ListEntitiesForPolicyResponse>"""


ATTACH_ROLE_POLICY_TEMPLATE = """<AttachRolePolicyResponse>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</AttachRolePolicyResponse>"""

DETACH_ROLE_POLICY_TEMPLATE = """<DetachRolePolicyResponse>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</DetachRolePolicyResponse>"""

ATTACH_USER_POLICY_TEMPLATE = """<AttachUserPolicyResponse>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</AttachUserPolicyResponse>"""

DETACH_USER_POLICY_TEMPLATE = """<DetachUserPolicyResponse>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</DetachUserPolicyResponse>"""

ATTACH_GROUP_POLICY_TEMPLATE = """<AttachGroupPolicyResponse>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</AttachGroupPolicyResponse>"""

DETACH_GROUP_POLICY_TEMPLATE = """<DetachGroupPolicyResponse>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</DetachGroupPolicyResponse>"""

CREATE_POLICY_TEMPLATE = """<CreatePolicyResponse>
  <CreatePolicyResult>
    <Policy>
      <Arn>{{ policy.arn }}</Arn>
      <AttachmentCount>{{ policy.attachment_count }}</AttachmentCount>
      <CreateDate>{{ policy.create_datetime }}</CreateDate>
      <DefaultVersionId>{{ policy.default_version_id }}</DefaultVersionId>
      <Path>{{ policy.path }}</Path>
      <PolicyId>{{ policy.id }}</PolicyId>
      <PolicyName>{{ policy.name }}</PolicyName>
      <UpdateDate>{{ policy.update_datetime }}</UpdateDate>
    </Policy>
  </CreatePolicyResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</CreatePolicyResponse>"""

GET_POLICY_TEMPLATE = """<GetPolicyResponse>
  <GetPolicyResult>
    <Policy>
      <PolicyName>{{ policy.name }}</PolicyName>
      <Description>{{ policy.description }}</Description>
      <DefaultVersionId>{{ policy.default_version_id }}</DefaultVersionId>
      <PolicyId>{{ policy.id }}</PolicyId>
      <Path>{{ policy.path }}</Path>
      <Arn>{{ policy.arn }}</Arn>
      <AttachmentCount>{{ policy.attachment_count }}</AttachmentCount>
      <CreateDate>{{ policy.create_datetime }}</CreateDate>
      <UpdateDate>{{ policy.update_datetime }}</UpdateDate>
    </Policy>
  </GetPolicyResult>
  <ResponseMetadata>
    <RequestId>684f0917-3d22-11e4-a4a0-cffb9EXAMPLE</RequestId>
  </ResponseMetadata>
</GetPolicyResponse>"""

LIST_ATTACHED_ROLE_POLICIES_TEMPLATE = """<ListAttachedRolePoliciesResponse>
  <ListAttachedRolePoliciesResult>
    {% if marker is none %}
    <IsTruncated>false</IsTruncated>
    {% else %}
    <IsTruncated>true</IsTruncated>
    <Marker>{{ marker }}</Marker>
    {% endif %}
    <AttachedPolicies>
      {% for policy in policies %}
      <member>
        <PolicyName>{{ policy.name }}</PolicyName>
        <PolicyArn>{{ policy.arn }}</PolicyArn>
      </member>
      {% endfor %}
    </AttachedPolicies>
  </ListAttachedRolePoliciesResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</ListAttachedRolePoliciesResponse>"""

LIST_ATTACHED_GROUP_POLICIES_TEMPLATE = """<ListAttachedGroupPoliciesResponse>
  <ListAttachedGroupPoliciesResult>
    {% if marker is none %}
    <IsTruncated>false</IsTruncated>
    {% else %}
    <IsTruncated>true</IsTruncated>
    <Marker>{{ marker }}</Marker>
    {% endif %}
    <AttachedPolicies>
      {% for policy in policies %}
      <member>
        <PolicyName>{{ policy.name }}</PolicyName>
        <PolicyArn>{{ policy.arn }}</PolicyArn>
      </member>
      {% endfor %}
    </AttachedPolicies>
  </ListAttachedGroupPoliciesResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</ListAttachedGroupPoliciesResponse>"""

LIST_ATTACHED_USER_POLICIES_TEMPLATE = """<ListAttachedUserPoliciesResponse>
  <ListAttachedUserPoliciesResult>
    {% if marker is none %}
    <IsTruncated>false</IsTruncated>
    {% else %}
    <IsTruncated>true</IsTruncated>
    <Marker>{{ marker }}</Marker>
    {% endif %}
    <AttachedPolicies>
      {% for policy in policies %}
      <member>
        <PolicyName>{{ policy.name }}</PolicyName>
        <PolicyArn>{{ policy.arn }}</PolicyArn>
      </member>
      {% endfor %}
    </AttachedPolicies>
  </ListAttachedUserPoliciesResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</ListAttachedUserPoliciesResponse>"""

LIST_POLICIES_TEMPLATE = """<ListPoliciesResponse>
  <ListPoliciesResult>
    {% if marker is none %}
    <IsTruncated>false</IsTruncated>
    {% else %}
    <IsTruncated>true</IsTruncated>
    <Marker>{{ marker }}</Marker>
    {% endif %}
    <Policies>
      {% for policy in policies %}
      <member>
        <Arn>{{ policy.arn }}</Arn>
        <AttachmentCount>{{ policy.attachment_count }}</AttachmentCount>
        <CreateDate>{{ policy.create_datetime.isoformat() }}</CreateDate>
        <DefaultVersionId>{{ policy.default_version_id }}</DefaultVersionId>
        <Path>{{ policy.path }}</Path>
        <PolicyId>{{ policy.id }}</PolicyId>
        <PolicyName>{{ policy.name }}</PolicyName>
        <UpdateDate>{{ policy.update_datetime.isoformat() }}</UpdateDate>
      </member>
      {% endfor %}
    </Policies>
  </ListPoliciesResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</ListPoliciesResponse>"""

GENERIC_EMPTY_TEMPLATE = """<{{ name }}Response>
   <ResponseMetadata>
      <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
   </ResponseMetadata>
</{{ name }}Response>"""

CREATE_INSTANCE_PROFILE_TEMPLATE = """<CreateInstanceProfileResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <CreateInstanceProfileResult>
    <InstanceProfile>
      <InstanceProfileId>{{ profile.id }}</InstanceProfileId>
      <Roles/>
      <InstanceProfileName>{{ profile.name }}</InstanceProfileName>
      <Path>{{ profile.path }}</Path>
      <Arn>{{ profile.arn }}</Arn>
      <CreateDate>{{ profile.create_date }}</CreateDate>
    </InstanceProfile>
  </CreateInstanceProfileResult>
  <ResponseMetadata>
    <RequestId>974142ee-99f1-11e1-a4c3-27EXAMPLE804</RequestId>
  </ResponseMetadata>
</CreateInstanceProfileResponse>"""

GET_INSTANCE_PROFILE_TEMPLATE = """<GetInstanceProfileResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetInstanceProfileResult>
    <InstanceProfile>
      <InstanceProfileId>{{ profile.id }}</InstanceProfileId>
      <Roles>
        {% for role in profile.roles %}
        <member>
          <Path>{{ role.path }}</Path>
          <Arn>{{ role.arn }}</Arn>
          <RoleName>{{ role.name }}</RoleName>
          <AssumeRolePolicyDocument>{{ role.assume_role_policy_document }}</AssumeRolePolicyDocument>
          <CreateDate>{{ role.create_date }}</CreateDate>
          <RoleId>{{ role.id }}</RoleId>
        </member>
        {% endfor %}
      </Roles>
      <InstanceProfileName>{{ profile.name }}</InstanceProfileName>
      <Path>{{ profile.path }}</Path>
      <Arn>{{ profile.arn }}</Arn>
      <CreateDate>{{ profile.create_date }}</CreateDate>
    </InstanceProfile>
  </GetInstanceProfileResult>
  <ResponseMetadata>
    <RequestId>37289fda-99f2-11e1-a4c3-27EXAMPLE804</RequestId>
  </ResponseMetadata>
</GetInstanceProfileResponse>"""

CREATE_ROLE_TEMPLATE = """<CreateRoleResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <CreateRoleResult>
    <Role>
      <Path>{{ role.path }}</Path>
      <Arn>{{ role.arn }}</Arn>
      <RoleName>{{ role.name }}</RoleName>
      <AssumeRolePolicyDocument>{{ role.assume_role_policy_document }}</AssumeRolePolicyDocument>
      <CreateDate>{{ role.create_date }}</CreateDate>
      <RoleId>{{ role.id }}</RoleId>
    </Role>
  </CreateRoleResult>
  <ResponseMetadata>
    <RequestId>4a93ceee-9966-11e1-b624-b1aEXAMPLE7c</RequestId>
  </ResponseMetadata>
</CreateRoleResponse>"""

GET_ROLE_POLICY_TEMPLATE = """<GetRolePolicyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
<GetRolePolicyResult>
  <PolicyName>{{ policy_name }}</PolicyName>
  <RoleName>{{ role_name }}</RoleName>
  <PolicyDocument>{{ policy_document }}</PolicyDocument>
</GetRolePolicyResult>
<ResponseMetadata>
  <RequestId>7e7cd8bc-99ef-11e1-a4c3-27EXAMPLE804</RequestId>
</ResponseMetadata>
</GetRolePolicyResponse>"""

UPDATE_ROLE_DESCRIPTION_TEMPLATE = """<UpdateRoleDescriptionResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <UpdateRoleDescriptionResult>
    <Role>
      <Path>{{ role.path }}</Path>
      <Arn>{{ role.arn }}</Arn>
      <RoleName>{{ role.name }}</RoleName>
      <AssumeRolePolicyDocument>{{ role.assume_role_policy_document }}</AssumeRolePolicyDocument>
      <CreateDate>{{ role.create_date }}</CreateDate>
      <RoleId>{{ role.id }}</RoleId>
      {% if role.tags %}
      <Tags>
        {% for tag in role.get_tags() %}
        <member>
            <Key>{{ tag['Key'] }}</Key>
            <Value>{{ tag['Value'] }}</Value>
        </member>
        {% endfor %}
      </Tags>
      {% endif %}
    </Role>
  </UpdateRoleDescriptionResult>
  <ResponseMetadata>
    <RequestId>df37e965-9967-11e1-a4c3-270EXAMPLE04</RequestId>
  </ResponseMetadata>
</UpdateRoleDescriptionResponse>"""

GET_ROLE_TEMPLATE = """<GetRoleResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetRoleResult>
    <Role>
      <Path>{{ role.path }}</Path>
      <Arn>{{ role.arn }}</Arn>
      <RoleName>{{ role.name }}</RoleName>
      <AssumeRolePolicyDocument>{{ role.assume_role_policy_document }}</AssumeRolePolicyDocument>
      <CreateDate>{{ role.create_date }}</CreateDate>
      <RoleId>{{ role.id }}</RoleId>
      {% if role.tags %}
      <Tags>
        {% for tag in role.get_tags() %}
        <member>
            <Key>{{ tag['Key'] }}</Key>
            <Value>{{ tag['Value'] }}</Value>
        </member>
        {% endfor %}
      </Tags>
      {% endif %}
    </Role>
  </GetRoleResult>
  <ResponseMetadata>
    <RequestId>df37e965-9967-11e1-a4c3-270EXAMPLE04</RequestId>
  </ResponseMetadata>
</GetRoleResponse>"""

ADD_ROLE_TO_INSTANCE_PROFILE_TEMPLATE = """<AddRoleToInstanceProfileResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>12657608-99f2-11e1-a4c3-27EXAMPLE804</RequestId>
  </ResponseMetadata>
</AddRoleToInstanceProfileResponse>"""

REMOVE_ROLE_FROM_INSTANCE_PROFILE_TEMPLATE = """<RemoveRoleFromInstanceProfileResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>12657608-99f2-11e1-a4c3-27EXAMPLE804</RequestId>
  </ResponseMetadata>
</RemoveRoleFromInstanceProfileResponse>"""

LIST_ROLES_TEMPLATE = """<ListRolesResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ListRolesResult>
    <IsTruncated>false</IsTruncated>
    <Roles>
      {% for role in roles %}
      <member>
        <Path>{{ role.path }}</Path>
        <Arn>{{ role.arn }}</Arn>
        <RoleName>{{ role.name }}</RoleName>
        <AssumeRolePolicyDocument>{{ role.assume_role_policy_document }}</AssumeRolePolicyDocument>
        <CreateDate>{{ role.create_date }}</CreateDate>
        <RoleId>{{ role.id }}</RoleId>
      </member>
      {% endfor %}
    </Roles>
  </ListRolesResult>
  <ResponseMetadata>
    <RequestId>20f7279f-99ee-11e1-a4c3-27EXAMPLE804</RequestId>
  </ResponseMetadata>
</ListRolesResponse>"""

LIST_ROLE_POLICIES = """<ListRolePoliciesResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
<ListRolePoliciesResult>
  <PolicyNames>
    {% for policy_name in role_policies %}
    <member>{{ policy_name }}</member>
    {% endfor %}
  </PolicyNames>
  <IsTruncated>false</IsTruncated>
</ListRolePoliciesResult>
<ResponseMetadata>
  <RequestId>8c7e1816-99f0-11e1-a4c3-27EXAMPLE804</RequestId>
</ResponseMetadata>
</ListRolePoliciesResponse>"""

CREATE_POLICY_VERSION_TEMPLATE = """<CreatePolicyVersionResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <CreatePolicyVersionResult>
    <PolicyVersion>
      <Document>{{ policy_version.document }}</Document>
      <VersionId>{{ policy_version.version_id }}</VersionId>
      <IsDefaultVersion>{{ policy_version.is_default }}</IsDefaultVersion>
      <CreateDate>{{ policy_version.create_datetime }}</CreateDate>
    </PolicyVersion>
  </CreatePolicyVersionResult>
  <ResponseMetadata>
    <RequestId>20f7279f-99ee-11e1-a4c3-27EXAMPLE804</RequestId>
  </ResponseMetadata>
</CreatePolicyVersionResponse>"""

GET_POLICY_VERSION_TEMPLATE = """<GetPolicyVersionResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetPolicyVersionResult>
    <PolicyVersion>
      <Document>{{ policy_version.document }}</Document>
      <VersionId>{{ policy_version.version_id }}</VersionId>
      <IsDefaultVersion>{{ policy_version.is_default }}</IsDefaultVersion>
      <CreateDate>{{ policy_version.create_datetime }}</CreateDate>
    </PolicyVersion>
  </GetPolicyVersionResult>
  <ResponseMetadata>
    <RequestId>20f7279f-99ee-11e1-a4c3-27EXAMPLE804</RequestId>
  </ResponseMetadata>
</GetPolicyVersionResponse>"""

LIST_POLICY_VERSIONS_TEMPLATE = """<ListPolicyVersionsResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ListPolicyVersionsResult>
    <IsTruncated>false</IsTruncated>
    <Versions>
      {% for policy_version in policy_versions %}
      <member>
        <Document>{{ policy_version.document }}</Document>
        <VersionId>{{ policy_version.version_id }}</VersionId>
        <IsDefaultVersion>{{ policy_version.is_default }}</IsDefaultVersion>
        <CreateDate>{{ policy_version.create_datetime }}</CreateDate>
      </member>
      {% endfor %}
    </Versions>
  </ListPolicyVersionsResult>
  <ResponseMetadata>
    <RequestId>20f7279f-99ee-11e1-a4c3-27EXAMPLE804</RequestId>
  </ResponseMetadata>
</ListPolicyVersionsResponse>"""

LIST_INSTANCE_PROFILES_TEMPLATE = """<ListInstanceProfilesResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ListInstanceProfilesResult>
    <IsTruncated>false</IsTruncated>
    <InstanceProfiles>
      {% for instance in instance_profiles %}
      <member>
        <InstanceProfileId>{{ instance.id }}</InstanceProfileId>
        <Roles>
          {% for role in instance.roles %}
          <member>
            <Path>{{ role.path }}</Path>
            <Arn>{{ role.arn }}</Arn>
            <RoleName>{{ role.name }}</RoleName>
            <AssumeRolePolicyDocument>{{ role.assume_role_policy_document }}</AssumeRolePolicyDocument>
            <CreateDate>{{ role.create_date }}</CreateDate>
            <RoleId>{{ role.id }}</RoleId>
          </member>
          {% endfor %}
        </Roles>
        <InstanceProfileName>{{ instance.name }}</InstanceProfileName>
        <Path>{{ instance.path }}</Path>
        <Arn>{{ instance.arn }}</Arn>
        <CreateDate>{{ instance.create_date }}</CreateDate>
      </member>
      {% endfor %}
    </InstanceProfiles>
  </ListInstanceProfilesResult>
  <ResponseMetadata>
    <RequestId>fd74fa8d-99f3-11e1-a4c3-27EXAMPLE804</RequestId>
  </ResponseMetadata>
</ListInstanceProfilesResponse>"""

UPLOAD_CERT_TEMPLATE = """<UploadServerCertificateResponse>
  <UploadServerCertificateResult>
    <ServerCertificateMetadata>
      <ServerCertificateName>{{ certificate.cert_name }}</ServerCertificateName>
      {% if certificate.path %}
      <Path>{{ certificate.path }}</Path>
      {% endif %}
      <Arn>{{ certificate.arn }}</Arn>
      <UploadDate>2010-05-08T01:02:03.004Z</UploadDate>
      <ServerCertificateId>ASCACKCEVSQ6C2EXAMPLE</ServerCertificateId>
      <Expiration>2012-05-08T01:02:03.004Z</Expiration>
    </ServerCertificateMetadata>
  </UploadServerCertificateResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</UploadServerCertificateResponse>"""

LIST_SERVER_CERTIFICATES_TEMPLATE = """<ListServerCertificatesResponse>
  <ListServerCertificatesResult>
    <IsTruncated>false</IsTruncated>
    <ServerCertificateMetadataList>
      {% for certificate in server_certificates %}
      <member>
        <ServerCertificateName>{{ certificate.cert_name }}</ServerCertificateName>
        {% if certificate.path %}
            <Path>{{ certificate.path }}</Path>
        {% endif %}
        <Arn>{{ certificate.arn }}</Arn>
        <UploadDate>2010-05-08T01:02:03.004Z</UploadDate>
        <ServerCertificateId>ASCACKCEVSQ6C2EXAMPLE</ServerCertificateId>
        <Expiration>2012-05-08T01:02:03.004Z</Expiration>
      </member>
      {% endfor %}
    </ServerCertificateMetadataList>
  </ListServerCertificatesResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</ListServerCertificatesResponse>"""

GET_SERVER_CERTIFICATE_TEMPLATE = """<GetServerCertificateResponse>
  <GetServerCertificateResult>
    <ServerCertificate>
      <ServerCertificateMetadata>
        <ServerCertificateName>{{ certificate.cert_name }}</ServerCertificateName>
        {% if certificate.path %}
            <Path>{{ certificate.path }}</Path>
        {% endif %}
        <Arn>{{ certificate.arn }}</Arn>
        <UploadDate>2010-05-08T01:02:03.004Z</UploadDate>
        <ServerCertificateId>ASCACKCEVSQ6C2EXAMPLE</ServerCertificateId>
        <Expiration>2012-05-08T01:02:03.004Z</Expiration>
      </ServerCertificateMetadata>
      <CertificateBody>{{ certificate.cert_body }}</CertificateBody>
    </ServerCertificate>
  </GetServerCertificateResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</GetServerCertificateResponse>"""

CREATE_GROUP_TEMPLATE = """<CreateGroupResponse>
   <CreateGroupResult>
      <Group>
         <Path>{{ group.path }}</Path>
         <GroupName>{{ group.name }}</GroupName>
         <GroupId>{{ group.id }}</GroupId>
         <Arn>{{ group.arn }}</Arn>
         <CreateDate>{{ group.create_date }}</CreateDate>
      </Group>
   </CreateGroupResult>
   <ResponseMetadata>
      <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
   </ResponseMetadata>
</CreateGroupResponse>"""

GET_GROUP_TEMPLATE = """<GetGroupResponse>
   <GetGroupResult>
      <Group>
         <Path>{{ group.path }}</Path>
         <GroupName>{{ group.name }}</GroupName>
         <GroupId>{{ group.id }}</GroupId>
         <Arn>{{ group.arn }}</Arn>
         <CreateDate>{{ group.create_date }}</CreateDate>
      </Group>
      <Users>
        {% for user in group.users %}
          <member>
            <Path>{{ user.path }}</Path>
            <UserName>{{ user.name }}</UserName>
            <UserId>{{ user.id }}</UserId>
            <Arn>{{ user.arn }}</Arn>
          </member>
        {% endfor %}
      </Users>
      <IsTruncated>false</IsTruncated>
   </GetGroupResult>
   <ResponseMetadata>
      <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
   </ResponseMetadata>
</GetGroupResponse>"""

LIST_GROUPS_TEMPLATE = """<ListGroupsResponse>
  <ListGroupsResult>
    <Groups>
        {% for group in groups %}
        <member>
            <Path>{{ group.path }}</Path>
            <GroupName>{{ group.name }}</GroupName>
            <GroupId>{{ group.id }}</GroupId>
            <Arn>{{ group.arn }}</Arn>
        </member>
        {% endfor %}
    </Groups>
    <IsTruncated>false</IsTruncated>
  </ListGroupsResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</ListGroupsResponse>"""

LIST_GROUPS_FOR_USER_TEMPLATE = """<ListGroupsForUserResponse>
  <ListGroupsForUserResult>
    <Groups>
        {% for group in groups %}
        <member>
            <Path>{{ group.path }}</Path>
            <GroupName>{{ group.name }}</GroupName>
            <GroupId>{{ group.id }}</GroupId>
            <Arn>{{ group.arn }}</Arn>
        </member>
        {% endfor %}
    </Groups>
    <IsTruncated>false</IsTruncated>
  </ListGroupsForUserResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</ListGroupsForUserResponse>"""

LIST_GROUP_POLICIES_TEMPLATE = """<ListGroupPoliciesResponse>
  <ListGroupPoliciesResult>
    {% if marker is none %}
    <IsTruncated>false</IsTruncated>
    {% else %}
    <IsTruncated>true</IsTruncated>
    <Marker>{{ marker }}</Marker>
    {% endif %}
    <PolicyNames>
    {% for policy in policies %}
        <member>{{ policy }}</member>
    {% endfor %}
    </PolicyNames>
  </ListGroupPoliciesResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</ListGroupPoliciesResponse>"""

GET_GROUP_POLICY_TEMPLATE = """<GetGroupPolicyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
<GetGroupPolicyResult>
  <PolicyName>{{ policy_name }}</PolicyName>
  <GroupName>{{ group_name }}</GroupName>
  <PolicyDocument>{{ policy_document }}</PolicyDocument>
</GetGroupPolicyResult>
<ResponseMetadata>
  <RequestId>7e7cd8bc-99ef-11e1-a4c3-27EXAMPLE804</RequestId>
</ResponseMetadata>
</GetGroupPolicyResponse>"""

USER_TEMPLATE = """<{{ action }}UserResponse>
   <{{ action }}UserResult>
      <User>
         <Path>{{ user.path }}</Path>
         <UserName>{{ user.name }}</UserName>
         <UserId>{{ user.id }}</UserId>
         <CreateDate>{{ user.created_iso_8601 }}</CreateDate>
         <Arn>{{ user.arn }}</Arn>
     </User>
   </{{ action }}UserResult>
   <ResponseMetadata>
      <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
   </ResponseMetadata>
</{{ action }}UserResponse>"""

LIST_USERS_TEMPLATE = """<{{ action }}UsersResponse>
   <{{ action }}UsersResult>
      <Users>
         {% for user in users %}
         <member>
             <UserId>{{ user.id }}</UserId>
             <Path>{{ user.path }}</Path>
             <UserName>{{ user.name }}</UserName>
             <CreateDate>{{ user.created_iso_8601 }}</CreateDate>
             <Arn>{{ user.arn }}</Arn>
         </member>
         {% endfor %}
     </Users>
   </{{ action }}UsersResult>
   <ResponseMetadata>
      <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
   </ResponseMetadata>
</{{ action }}UsersResponse>"""

CREATE_LOGIN_PROFILE_TEMPLATE = """<CreateLoginProfileResponse>
   <CreateLoginProfileResult>
      <LoginProfile>
         <UserName>{{ user.name }}</UserName>
         <CreateDate>{{ user.created_iso_8601 }}</CreateDate>
      </LoginProfile>
   </CreateLoginProfileResult>
   <ResponseMetadata>
      <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
   </ResponseMetadata>
</CreateLoginProfileResponse>
"""

GET_LOGIN_PROFILE_TEMPLATE = """<GetLoginProfileResponse>
   <GetLoginProfileResult>
      <LoginProfile>
         <UserName>{{ user.name }}</UserName>
         <CreateDate>{{ user.created_iso_8601 }}</CreateDate>
         {% if user.password_reset_required %}
         <PasswordResetRequired>true</PasswordResetRequired>
         {% endif %}
      </LoginProfile>
   </GetLoginProfileResult>
   <ResponseMetadata>
      <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
   </ResponseMetadata>
</GetLoginProfileResponse>
"""

UPDATE_LOGIN_PROFILE_TEMPLATE = """<UpdateLoginProfileResponse>
   <ResponseMetadata>
      <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
   </ResponseMetadata>
</UpdateLoginProfileResponse>
"""

GET_USER_POLICY_TEMPLATE = """<GetUserPolicyResponse>
   <GetUserPolicyResult>
      <UserName>{{ user_name }}</UserName>
      <PolicyName>{{ policy_name }}</PolicyName>
      <PolicyDocument>
      {{ policy_document }}
      </PolicyDocument>
   </GetUserPolicyResult>
   <ResponseMetadata>
      <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
   </ResponseMetadata>
</GetUserPolicyResponse>"""

LIST_USER_POLICIES_TEMPLATE = """<ListUserPoliciesResponse>
   <ListUserPoliciesResult>
      <PolicyNames>
        {% for policy in policies %}
         <member>{{ policy }}</member>
        {% endfor %}
      </PolicyNames>
      <IsTruncated>false</IsTruncated>
   </ListUserPoliciesResult>
   <ResponseMetadata>
      <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
   </ResponseMetadata>
</ListUserPoliciesResponse>"""

CREATE_ACCESS_KEY_TEMPLATE = """<CreateAccessKeyResponse>
   <CreateAccessKeyResult>
     <AccessKey>
         <UserName>{{ key.user_name }}</UserName>
         <AccessKeyId>{{ key.access_key_id }}</AccessKeyId>
         <Status>{{ key.status }}</Status>
         <SecretAccessKey>{{ key.secret_access_key }}</SecretAccessKey>
      </AccessKey>
   </CreateAccessKeyResult>
   <ResponseMetadata>
      <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
   </ResponseMetadata>
</CreateAccessKeyResponse>"""

LIST_ACCESS_KEYS_TEMPLATE = """<ListAccessKeysResponse>
   <ListAccessKeysResult>
      <UserName>{{ user_name }}</UserName>
      <AccessKeyMetadata>
        {% for key in keys %}
         <member>
            <UserName>{{ user_name }}</UserName>
            <AccessKeyId>{{ key.access_key_id }}</AccessKeyId>
            <Status>{{ key.status }}</Status>
            <CreateDate>{{ key.create_date }}</CreateDate>
         </member>
        {% endfor %}
      </AccessKeyMetadata>
      <IsTruncated>false</IsTruncated>
   </ListAccessKeysResult>
   <ResponseMetadata>
      <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
   </ResponseMetadata>
</ListAccessKeysResponse>"""


GET_ACCESS_KEY_LAST_USED_TEMPLATE = """
<GetAccessKeyLastUsedResponse>
    <GetAccessKeyLastUsedResult>
        <UserName>{{ user_name }}</UserName>
        <AccessKeyLastUsed>
            <LastUsedDate>{{ last_used }}</LastUsedDate>
        </AccessKeyLastUsed>
    </GetAccessKeyLastUsedResult>
</GetAccessKeyLastUsedResponse>
"""

CREDENTIAL_REPORT_GENERATING = """
<GenerateCredentialReportResponse>
    <GenerateCredentialReportResult>
        <State>STARTED</State>
        <Description>No report exists. Starting a new report generation task</Description>
    </GenerateCredentialReportResult>
    <ResponseMetadata>
        <RequestId>fa788a82-aa8a-11e4-a278-1786c418872b"</RequestId>
    </ResponseMetadata>
</GenerateCredentialReportResponse>"""

CREDENTIAL_REPORT_GENERATED = """<GenerateCredentialReportResponse>
    <GenerateCredentialReportResult>
        <State>COMPLETE</State>
    </GenerateCredentialReportResult>
    <ResponseMetadata>
        <RequestId>fa788a82-aa8a-11e4-a278-1786c418872b"</RequestId>
    </ResponseMetadata>
</GenerateCredentialReportResponse>"""

CREDENTIAL_REPORT = """<GetCredentialReportResponse>
    <GetCredentialReportResult>
        <Content>{{ report }}</Content>
        <GeneratedTime>2015-02-02T20:02:02Z</GeneratedTime>
        <ReportFormat>text/csv</ReportFormat>
    </GetCredentialReportResult>
    <ResponseMetadata>
        <RequestId>fa788a82-aa8a-11e4-a278-1786c418872b"</RequestId>
    </ResponseMetadata>
</GetCredentialReportResponse>"""

LIST_INSTANCE_PROFILES_FOR_ROLE_TEMPLATE = """<ListInstanceProfilesForRoleResponse>
<ListInstanceProfilesForRoleResult>
  <IsTruncated>false</IsTruncated>
  <InstanceProfiles>
    {% for profile in instance_profiles %}
    <member>
    <InstanceProfileId>{{ profile.id }}</InstanceProfileId>
    <Roles>
      {% for role in profile.roles %}
      <member>
        <Path>{{ role.path }}</Path>
        <Arn>{{ role.arn }}</Arn>
        <RoleName>{{ role.name }}</RoleName>
        <AssumeRolePolicyDocument>{{ role.assume_policy_document }}</AssumeRolePolicyDocument>
        <CreateDate>{{ role.create_date }}</CreateDate>
        <RoleId>{{ role.id }}</RoleId>
      </member>
      {% endfor %}
    </Roles>
    <InstanceProfileName>{{ profile.name }}</InstanceProfileName>
    <Path>{{ profile.path }}</Path>
    <Arn>{{ profile.arn }}</Arn>
    <CreateDate>{{ profile.create_date }}</CreateDate>
    </member>
    {% endfor %}
  </InstanceProfiles>
</ListInstanceProfilesForRoleResult>
<ResponseMetadata>
  <RequestId>6a8c3992-99f4-11e1-a4c3-27EXAMPLE804</RequestId>
</ResponseMetadata>
</ListInstanceProfilesForRoleResponse>"""

LIST_MFA_DEVICES_TEMPLATE = """<ListMFADevicesResponse>
   <ListMFADevicesResult>
      <MFADevices>
        {% for device in devices %}
         <member>
            <UserName>{{ user_name }}</UserName>
            <SerialNumber>{{ device.serial_number }}</SerialNumber>
         </member>
        {% endfor %}
      </MFADevices>
      <IsTruncated>false</IsTruncated>
   </ListMFADevicesResult>
   <ResponseMetadata>
      <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
   </ResponseMetadata>
</ListMFADevicesResponse>"""


LIST_ACCOUNT_ALIASES_TEMPLATE = """<ListAccountAliasesResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
<ListAccountAliasesResult>
  <IsTruncated>false</IsTruncated>
  <AccountAliases>
    {% for alias in aliases %}
    <member>{{ alias }}</member>
    {% endfor %}
  </AccountAliases>
</ListAccountAliasesResult>
<ResponseMetadata>
  <RequestId>c5a076e9-f1b0-11df-8fbe-45274EXAMPLE</RequestId>
</ResponseMetadata>
</ListAccountAliasesResponse>"""


CREATE_ACCOUNT_ALIAS_TEMPLATE = """<CreateAccountAliasResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>36b5db08-f1b0-11df-8fbe-45274EXAMPLE</RequestId>
  </ResponseMetadata>
</CreateAccountAliasResponse>"""


DELETE_ACCOUNT_ALIAS_TEMPLATE = """<DeleteAccountAliasResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</DeleteAccountAliasResponse>"""


LIST_GROUPS_FOR_USER_TEMPLATE = """<ListGroupsForUserResponse>
  <ListGroupsForUserResult>
    <Groups>
        {% for group in groups %}
        <member>
            <Path>{{ group.path }}</Path>
            <GroupName>{{ group.name }}</GroupName>
            <GroupId>{{ group.id }}</GroupId>
            <Arn>{{ group.arn }}</Arn>
        </member>
        {% endfor %}
    </Groups>
    <IsTruncated>false</IsTruncated>
  </ListGroupsForUserResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</ListGroupsForUserResponse>"""


GET_ACCOUNT_AUTHORIZATION_DETAILS_TEMPLATE = """<GetAccountAuthorizationDetailsResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetAccountAuthorizationDetailsResult>
    <IsTruncated>false</IsTruncated>
    <UserDetailList>
    {% for user in users %}
      <member>
        <GroupList>
        {% for group in get_groups_for_user(user.name) %}
          <member>{{ group.name }}</member>
        {% endfor %}
        </GroupList>
        <AttachedManagedPolicies>
        {% for policy in user.managed_policies %}
          <member>
            <PolicyName>{{ user.managed_policies[policy].name }}</PolicyName>
            <PolicyArn>{{ policy }}</PolicyArn>
          </member>
        {% endfor %}
        </AttachedManagedPolicies>
        <UserId>{{ user.id }}</UserId>
        <Path>{{ user.path }}</Path>
        <UserName>{{ user.name }}</UserName>
        <Arn>{{ user.arn }}</Arn>
        <CreateDate>{{ user.created_iso_8601 }}</CreateDate>
      </member>
    {% endfor %}
    </UserDetailList>
    <GroupDetailList>
    {% for group in groups %}
      <member>
        <GroupId>{{ group.id }}</GroupId>
        <AttachedManagedPolicies>
          {% for policy_arn in group.managed_policies %}
            <member>
                <PolicyName>{{ group.managed_policies[policy_arn].name }}</PolicyName>
                <PolicyArn>{{ policy_arn }}</PolicyArn>
            </member>
          {% endfor %}
        </AttachedManagedPolicies>
        <GroupName>{{ group.name }}</GroupName>
        <Path>{{ group.path }}</Path>
        <Arn>{{ group.arn }}</Arn>
        <CreateDate>{{ group.create_date }}</CreateDate>
        <GroupPolicyList>
        {% for policy in group.policies %}
            <member>
                <PolicyName>{{ policy }}</PolicyName>
                <PolicyDocument>{{ group.get_policy(policy) }}</PolicyDocument>
            </member>
        {% endfor %}
        </GroupPolicyList>
      </member>
    {% endfor %}
    </GroupDetailList>
    <RoleDetailList>
    {% for role in roles %}
      <member>
        <RolePolicyList>
        {% for inline_policy in role.policies %}
            <member>
                <PolicyName>{{ inline_policy }}</PolicyName>
                <PolicyDocument>{{ role.policies[inline_policy] }}</PolicyDocument>
            </member>
        {% endfor %}
        </RolePolicyList>
        <AttachedManagedPolicies>
        {% for policy_arn in role.managed_policies %}
            <member>
                <PolicyName>{{ role.managed_policies[policy_arn].name }}</PolicyName>
                <PolicyArn>{{ policy_arn }}</PolicyArn>
            </member>
        {% endfor %}
        </AttachedManagedPolicies>
        <Tags>
        {% for tag in role.get_tags() %}
        <member>
            <Key>{{ tag['Key'] }}</Key>
            <Value>{{ tag['Value'] }}</Value>
        </member>
        {% endfor %}
        </Tags>
        <InstanceProfileList>
            {% for profile in instance_profiles %}
            <member>
            <InstanceProfileId>{{ profile.id }}</InstanceProfileId>
            <Roles>
              {% for role in profile.roles %}
              <member>
                <Path>{{ role.path }}</Path>
                <Arn>{{ role.arn }}</Arn>
                <RoleName>{{ role.name }}</RoleName>
                <AssumeRolePolicyDocument>{{ role.assume_role_policy_document }}</AssumeRolePolicyDocument>
                <CreateDate>{{ role.create_date }}</CreateDate>
                <RoleId>{{ role.id }}</RoleId>
              </member>
              {% endfor %}
            </Roles>
            <InstanceProfileName>{{ profile.name }}</InstanceProfileName>
            <Path>{{ profile.path }}</Path>
            <Arn>{{ profile.arn }}</Arn>
            <CreateDate>{{ profile.create_date }}</CreateDate>
            </member>
            {% endfor %}
        </InstanceProfileList>
        <Path>{{ role.path }}</Path>
        <Arn>{{ role.arn }}</Arn>
        <RoleName>{{ role.name }}</RoleName>
        <AssumeRolePolicyDocument>{{ role.assume_role_policy_document }}</AssumeRolePolicyDocument>
        <CreateDate>{{ role.create_date }}</CreateDate>
        <RoleId>{{ role.id }}</RoleId>
      </member>
    {% endfor %}
    </RoleDetailList>
    <Policies>
    {% for policy in policies %}
      <member>
        <PolicyName>{{ policy.name }}</PolicyName>
        <DefaultVersionId>{{ policy.default_version_id }}</DefaultVersionId>
        <PolicyId>{{ policy.id }}</PolicyId>
        <Path>{{ policy.path }}</Path>
        <PolicyVersionList>
        {% for policy_version in policy.versions %}
          <member>
            <Document>{{ policy_version.document }}</Document>
            <IsDefaultVersion>{{ policy_version.is_default }}</IsDefaultVersion>
            <VersionId>{{ policy_version.version_id }}</VersionId>
            <CreateDate>{{ policy_version.create_datetime }}</CreateDate>
          </member>
        {% endfor %}
        </PolicyVersionList>
        <Arn>{{ policy.arn }}</Arn>
        <AttachmentCount>1</AttachmentCount>
        <CreateDate>{{ policy.create_datetime }}</CreateDate>
        <IsAttachable>true</IsAttachable>
        <UpdateDate>{{ policy.update_datetime }}</UpdateDate>
      </member>
    {% endfor %}
    </Policies>
  </GetAccountAuthorizationDetailsResult>
  <ResponseMetadata>
    <RequestId>92e79ae7-7399-11e4-8c85-4b53eEXAMPLE</RequestId>
  </ResponseMetadata>
</GetAccountAuthorizationDetailsResponse>"""

CREATE_SAML_PROVIDER_TEMPLATE = """<CreateSAMLProviderResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <CreateSAMLProviderResult>
    <SAMLProviderArn>{{ saml_provider.arn }}</SAMLProviderArn>
  </CreateSAMLProviderResult>
  <ResponseMetadata>
    <RequestId>29f47818-99f5-11e1-a4c3-27EXAMPLE804</RequestId>
  </ResponseMetadata>
</CreateSAMLProviderResponse>"""

LIST_SAML_PROVIDERS_TEMPLATE = """<ListSAMLProvidersResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
<ListSAMLProvidersResult>
  <SAMLProviderList>
    {% for saml_provider in saml_providers %}
    <member>
      <Arn>{{ saml_provider.arn }}</Arn>
      <ValidUntil>2032-05-09T16:27:11Z</ValidUntil>
      <CreateDate>2012-05-09T16:27:03Z</CreateDate>
    </member>
    {% endfor %}
  </SAMLProviderList>
</ListSAMLProvidersResult>
<ResponseMetadata>
  <RequestId>fd74fa8d-99f3-11e1-a4c3-27EXAMPLE804</RequestId>
</ResponseMetadata>
</ListSAMLProvidersResponse>"""

GET_SAML_PROVIDER_TEMPLATE = """<GetSAMLProviderResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
<GetSAMLProviderResult>
  <CreateDate>2012-05-09T16:27:11Z</CreateDate>
  <ValidUntil>2015-12-31T21:59:59Z</ValidUntil>
  <SAMLMetadataDocument>{{ saml_provider.saml_metadata_document }}</SAMLMetadataDocument>
</GetSAMLProviderResult>
<ResponseMetadata>
  <RequestId>29f47818-99f5-11e1-a4c3-27EXAMPLE804</RequestId>
</ResponseMetadata>
</GetSAMLProviderResponse>"""

DELETE_SAML_PROVIDER_TEMPLATE = """<DeleteSAMLProviderResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>c749ee7f-99ef-11e1-a4c3-27EXAMPLE804</RequestId>
  </ResponseMetadata>
</DeleteSAMLProviderResponse>"""

UPDATE_SAML_PROVIDER_TEMPLATE = """<UpdateSAMLProviderResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
<UpdateSAMLProviderResult>
  <SAMLProviderArn>{{ saml_provider.arn }}</SAMLProviderArn>
</UpdateSAMLProviderResult>
<ResponseMetadata>
  <RequestId>29f47818-99f5-11e1-a4c3-27EXAMPLE804</RequestId>
</ResponseMetadata>
</UpdateSAMLProviderResponse>"""

UPLOAD_SIGNING_CERTIFICATE_TEMPLATE = """<UploadSigningCertificateResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <UploadSigningCertificateResult>
    <Certificate>
      <UserName>{{ cert.user_name }}</UserName>
      <CertificateId>{{ cert.id }}</CertificateId>
      <CertificateBody>{{ cert.body }}</CertificateBody>
      <Status>{{ cert.status }}</Status>
    </Certificate>
 </UploadSigningCertificateResult>
 <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
 </ResponseMetadata>
</UploadSigningCertificateResponse>"""


UPDATE_SIGNING_CERTIFICATE_TEMPLATE = """<UpdateSigningCertificateResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
 <ResponseMetadata>
    <RequestId>EXAMPLE8-90ab-cdef-fedc-ba987EXAMPLE</RequestId>
 </ResponseMetadata>
</UpdateSigningCertificateResponse>"""


DELETE_SIGNING_CERTIFICATE_TEMPLATE = """<DeleteSigningCertificateResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</DeleteSigningCertificateResponse>"""


LIST_SIGNING_CERTIFICATES_TEMPLATE = """<ListSigningCertificatesResponse>
  <ListSigningCertificatesResult>
    <UserName>{{ user_name }}</UserName>
    <Certificates>
       {% for cert in certificates %}
       <member>
          <UserName>{{ user_name }}</UserName>
          <CertificateId>{{ cert.id }}</CertificateId>
          <CertificateBody>{{ cert.body }}</CertificateBody>
          <Status>{{ cert.status }}</Status>
       </member>
       {% endfor %}
    </Certificates>
    <IsTruncated>false</IsTruncated>
 </ListSigningCertificatesResult>
 <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
 </ResponseMetadata>
</ListSigningCertificatesResponse>"""


TAG_ROLE_TEMPLATE = """<TagRoleResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>EXAMPLE8-90ab-cdef-fedc-ba987EXAMPLE</RequestId>
  </ResponseMetadata>
</TagRoleResponse>"""


LIST_ROLE_TAG_TEMPLATE = """<ListRoleTagsResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ListRoleTagsResult>
    <IsTruncated>{{ 'true' if marker else 'false' }}</IsTruncated>
    {% if marker %}
    <Marker>{{ marker }}</Marker>
    {% endif %}
    <Tags>
      {% for tag in tags %}
      <member>
        <Key>{{ tag['Key'] }}</Key>
        <Value>{{ tag['Value'] }}</Value>
      </member>
      {% endfor %}
    </Tags>
  </ListRoleTagsResult>
  <ResponseMetadata>
    <RequestId>EXAMPLE8-90ab-cdef-fedc-ba987EXAMPLE</RequestId>
  </ResponseMetadata>
</ListRoleTagsResponse>"""


UNTAG_ROLE_TEMPLATE = """<UntagRoleResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>EXAMPLE8-90ab-cdef-fedc-ba987EXAMPLE</RequestId>
  </ResponseMetadata>
</UntagRoleResponse>"""
