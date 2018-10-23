"""
    SoftLayer.CLI.routes
    ~~~~~~~~~~~~~~~~~~~~~
    This is how all commands are registered with the CLI.

    :license: MIT, see LICENSE for more details.
"""

ALL_ROUTES = [
    ('shell', 'SoftLayer.shell.core:cli'),

    ('call-api', 'SoftLayer.CLI.call_api:cli'),

    ('virtual', 'SoftLayer.CLI.virt'),
    ('virtual:cancel', 'SoftLayer.CLI.virt.cancel:cli'),
    ('virtual:capture', 'SoftLayer.CLI.virt.capture:cli'),
    ('virtual:create', 'SoftLayer.CLI.virt.create:cli'),
    ('virtual:create-options', 'SoftLayer.CLI.virt.create_options:cli'),
    ('virtual:detail', 'SoftLayer.CLI.virt.detail:cli'),
    ('virtual:dns-sync', 'SoftLayer.CLI.virt.dns:cli'),
    ('virtual:edit', 'SoftLayer.CLI.virt.edit:cli'),
    ('virtual:list', 'SoftLayer.CLI.virt.list:cli'),
    ('virtual:pause', 'SoftLayer.CLI.virt.power:pause'),
    ('virtual:power-off', 'SoftLayer.CLI.virt.power:power_off'),
    ('virtual:power-on', 'SoftLayer.CLI.virt.power:power_on'),
    ('virtual:rescue', 'SoftLayer.CLI.virt.power:rescue'),
    ('virtual:resume', 'SoftLayer.CLI.virt.power:resume'),
    ('virtual:ready', 'SoftLayer.CLI.virt.ready:cli'),
    ('virtual:reboot', 'SoftLayer.CLI.virt.power:reboot'),
    ('virtual:reload', 'SoftLayer.CLI.virt.reload:cli'),
    ('virtual:upgrade', 'SoftLayer.CLI.virt.upgrade:cli'),
    ('virtual:credentials', 'SoftLayer.CLI.virt.credentials:cli'),
    ('virtual:capacity', 'SoftLayer.CLI.virt.capacity:cli'),

    ('dedicatedhost', 'SoftLayer.CLI.dedicatedhost'),
    ('dedicatedhost:list', 'SoftLayer.CLI.dedicatedhost.list:cli'),
    ('dedicatedhost:create', 'SoftLayer.CLI.dedicatedhost.create:cli'),
    ('dedicatedhost:create-options', 'SoftLayer.CLI.dedicatedhost.create_options:cli'),
    ('dedicatedhost:detail', 'SoftLayer.CLI.dedicatedhost.detail:cli'),
    ('dedicatedhost:cancel', 'SoftLayer.CLI.dedicatedhost.cancel:cli'),

    ('cdn', 'SoftLayer.CLI.cdn'),
    ('cdn:detail', 'SoftLayer.CLI.cdn.detail:cli'),
    ('cdn:list', 'SoftLayer.CLI.cdn.list:cli'),
    ('cdn:load', 'SoftLayer.CLI.cdn.load:cli'),
    ('cdn:origin-add', 'SoftLayer.CLI.cdn.origin_add:cli'),
    ('cdn:origin-list', 'SoftLayer.CLI.cdn.origin_list:cli'),
    ('cdn:origin-remove', 'SoftLayer.CLI.cdn.origin_remove:cli'),
    ('cdn:purge', 'SoftLayer.CLI.cdn.purge:cli'),

    ('config', 'SoftLayer.CLI.config'),
    ('config:setup', 'SoftLayer.CLI.config.setup:cli'),
    ('config:show', 'SoftLayer.CLI.config.show:cli'),
    ('setup', 'SoftLayer.CLI.config.setup:cli'),

    ('dns', 'SoftLayer.CLI.dns'),
    ('dns:import', 'SoftLayer.CLI.dns.zone_import:cli'),
    ('dns:record-add', 'SoftLayer.CLI.dns.record_add:cli'),
    ('dns:record-edit', 'SoftLayer.CLI.dns.record_edit:cli'),
    ('dns:record-list', 'SoftLayer.CLI.dns.record_list:cli'),
    ('dns:record-remove', 'SoftLayer.CLI.dns.record_remove:cli'),
    ('dns:zone-create', 'SoftLayer.CLI.dns.zone_create:cli'),
    ('dns:zone-delete', 'SoftLayer.CLI.dns.zone_delete:cli'),
    ('dns:zone-list', 'SoftLayer.CLI.dns.zone_list:cli'),
    ('dns:zone-print', 'SoftLayer.CLI.dns.zone_print:cli'),

    ('block', 'SoftLayer.CLI.block'),
    ('block:access-authorize', 'SoftLayer.CLI.block.access.authorize:cli'),
    ('block:access-list', 'SoftLayer.CLI.block.access.list:cli'),
    ('block:access-revoke', 'SoftLayer.CLI.block.access.revoke:cli'),
    ('block:access-password', 'SoftLayer.CLI.block.access.password:cli'),
    ('block:replica-failback', 'SoftLayer.CLI.block.replication.failback:cli'),
    ('block:replica-failover', 'SoftLayer.CLI.block.replication.failover:cli'),
    ('block:replica-order', 'SoftLayer.CLI.block.replication.order:cli'),
    ('block:replica-partners', 'SoftLayer.CLI.block.replication.partners:cli'),
    ('block:replica-locations',
     'SoftLayer.CLI.block.replication.locations:cli'),
    ('block:snapshot-cancel', 'SoftLayer.CLI.block.snapshot.cancel:cli'),
    ('block:snapshot-create', 'SoftLayer.CLI.block.snapshot.create:cli'),
    ('block:snapshot-delete', 'SoftLayer.CLI.block.snapshot.delete:cli'),
    ('block:snapshot-disable', 'SoftLayer.CLI.block.snapshot.disable:cli'),
    ('block:snapshot-enable', 'SoftLayer.CLI.block.snapshot.enable:cli'),
    ('block:snapshot-schedule-list',
     'SoftLayer.CLI.block.snapshot.schedule_list:cli'),
    ('block:snapshot-list', 'SoftLayer.CLI.block.snapshot.list:cli'),
    ('block:snapshot-order', 'SoftLayer.CLI.block.snapshot.order:cli'),
    ('block:snapshot-restore', 'SoftLayer.CLI.block.snapshot.restore:cli'),
    ('block:volume-cancel', 'SoftLayer.CLI.block.cancel:cli'),
    ('block:volume-count', 'SoftLayer.CLI.block.count:cli'),
    ('block:volume-detail', 'SoftLayer.CLI.block.detail:cli'),
    ('block:volume-duplicate', 'SoftLayer.CLI.block.duplicate:cli'),
    ('block:volume-list', 'SoftLayer.CLI.block.list:cli'),
    ('block:volume-modify', 'SoftLayer.CLI.block.modify:cli'),
    ('block:volume-order', 'SoftLayer.CLI.block.order:cli'),
    ('block:volume-set-lun-id', 'SoftLayer.CLI.block.lun:cli'),

    ('file', 'SoftLayer.CLI.file'),
    ('file:access-authorize', 'SoftLayer.CLI.file.access.authorize:cli'),
    ('file:access-list', 'SoftLayer.CLI.file.access.list:cli'),
    ('file:access-revoke', 'SoftLayer.CLI.file.access.revoke:cli'),
    ('file:replica-failback', 'SoftLayer.CLI.file.replication.failback:cli'),
    ('file:replica-failover', 'SoftLayer.CLI.file.replication.failover:cli'),
    ('file:replica-order', 'SoftLayer.CLI.file.replication.order:cli'),
    ('file:replica-partners', 'SoftLayer.CLI.file.replication.partners:cli'),
    ('file:replica-locations', 'SoftLayer.CLI.file.replication.locations:cli'),
    ('file:snapshot-cancel', 'SoftLayer.CLI.file.snapshot.cancel:cli'),
    ('file:snapshot-create', 'SoftLayer.CLI.file.snapshot.create:cli'),
    ('file:snapshot-delete', 'SoftLayer.CLI.file.snapshot.delete:cli'),
    ('file:snapshot-disable', 'SoftLayer.CLI.file.snapshot.disable:cli'),
    ('file:snapshot-enable', 'SoftLayer.CLI.file.snapshot.enable:cli'),
    ('file:snapshot-schedule-list',
     'SoftLayer.CLI.file.snapshot.schedule_list:cli'),
    ('file:snapshot-list', 'SoftLayer.CLI.file.snapshot.list:cli'),
    ('file:snapshot-order', 'SoftLayer.CLI.file.snapshot.order:cli'),
    ('file:snapshot-restore', 'SoftLayer.CLI.file.snapshot.restore:cli'),
    ('file:volume-cancel', 'SoftLayer.CLI.file.cancel:cli'),
    ('file:volume-count', 'SoftLayer.CLI.file.count:cli'),
    ('file:volume-detail', 'SoftLayer.CLI.file.detail:cli'),
    ('file:volume-duplicate', 'SoftLayer.CLI.file.duplicate:cli'),
    ('file:volume-list', 'SoftLayer.CLI.file.list:cli'),
    ('file:volume-modify', 'SoftLayer.CLI.file.modify:cli'),
    ('file:volume-order', 'SoftLayer.CLI.file.order:cli'),

    ('firewall', 'SoftLayer.CLI.firewall'),
    ('firewall:add', 'SoftLayer.CLI.firewall.add:cli'),
    ('firewall:cancel', 'SoftLayer.CLI.firewall.cancel:cli'),
    ('firewall:detail', 'SoftLayer.CLI.firewall.detail:cli'),
    ('firewall:edit', 'SoftLayer.CLI.firewall.edit:cli'),
    ('firewall:list', 'SoftLayer.CLI.firewall.list:cli'),

    ('globalip', 'SoftLayer.CLI.globalip'),
    ('globalip:assign', 'SoftLayer.CLI.globalip.assign:cli'),
    ('globalip:cancel', 'SoftLayer.CLI.globalip.cancel:cli'),
    ('globalip:create', 'SoftLayer.CLI.globalip.create:cli'),
    ('globalip:list', 'SoftLayer.CLI.globalip.list:cli'),
    ('globalip:unassign', 'SoftLayer.CLI.globalip.unassign:cli'),

    ('image', 'SoftLayer.CLI.image'),
    ('image:delete', 'SoftLayer.CLI.image.delete:cli'),
    ('image:detail', 'SoftLayer.CLI.image.detail:cli'),
    ('image:edit', 'SoftLayer.CLI.image.edit:cli'),
    ('image:list', 'SoftLayer.CLI.image.list:cli'),
    ('image:import', 'SoftLayer.CLI.image.import:cli'),
    ('image:export', 'SoftLayer.CLI.image.export:cli'),

    ('ipsec', 'SoftLayer.CLI.vpn.ipsec'),
    ('ipsec:configure', 'SoftLayer.CLI.vpn.ipsec.configure:cli'),
    ('ipsec:detail', 'SoftLayer.CLI.vpn.ipsec.detail:cli'),
    ('ipsec:list', 'SoftLayer.CLI.vpn.ipsec.list:cli'),
    ('ipsec:subnet-add', 'SoftLayer.CLI.vpn.ipsec.subnet.add:cli'),
    ('ipsec:subnet-remove', 'SoftLayer.CLI.vpn.ipsec.subnet.remove:cli'),
    ('ipsec:translation-add', 'SoftLayer.CLI.vpn.ipsec.translation.add:cli'),
    ('ipsec:translation-remove',
     'SoftLayer.CLI.vpn.ipsec.translation.remove:cli'),
    ('ipsec:translation-update',
     'SoftLayer.CLI.vpn.ipsec.translation.update:cli'),
    ('ipsec:update', 'SoftLayer.CLI.vpn.ipsec.update:cli'),

    ('loadbal', 'SoftLayer.CLI.loadbal'),
    ('loadbal:cancel', 'SoftLayer.CLI.loadbal.cancel:cli'),
    ('loadbal:create', 'SoftLayer.CLI.loadbal.create:cli'),
    ('loadbal:create-options', 'SoftLayer.CLI.loadbal.create_options:cli'),
    ('loadbal:detail', 'SoftLayer.CLI.loadbal.detail:cli'),
    ('loadbal:group-add', 'SoftLayer.CLI.loadbal.group_add:cli'),
    ('loadbal:group-delete', 'SoftLayer.CLI.loadbal.group_delete:cli'),
    ('loadbal:group-edit', 'SoftLayer.CLI.loadbal.group_edit:cli'),
    ('loadbal:group-reset', 'SoftLayer.CLI.loadbal.group_reset:cli'),
    ('loadbal:health-checks', 'SoftLayer.CLI.loadbal.health_checks:cli'),
    ('loadbal:list', 'SoftLayer.CLI.loadbal.list:cli'),
    ('loadbal:routing-methods', 'SoftLayer.CLI.loadbal.routing_methods:cli'),
    ('loadbal:routing-types', 'SoftLayer.CLI.loadbal.routing_types:cli'),
    ('loadbal:service-add', 'SoftLayer.CLI.loadbal.service_add:cli'),
    ('loadbal:service-delete', 'SoftLayer.CLI.loadbal.service_delete:cli'),
    ('loadbal:service-edit', 'SoftLayer.CLI.loadbal.service_edit:cli'),
    ('loadbal:service-toggle', 'SoftLayer.CLI.loadbal.service_toggle:cli'),

    ('messaging', 'SoftLayer.CLI.mq'),
    ('messaging:accounts-list', 'SoftLayer.CLI.mq.accounts_list:cli'),
    ('messaging:endpoints-list', 'SoftLayer.CLI.mq.endpoints_list:cli'),
    ('messaging:ping', 'SoftLayer.CLI.mq.ping:cli'),
    ('messaging:queue-add', 'SoftLayer.CLI.mq.queue_add:cli'),
    ('messaging:queue-detail', 'SoftLayer.CLI.mq.queue_detail:cli'),
    ('messaging:queue-edit', 'SoftLayer.CLI.mq.queue_edit:cli'),
    ('messaging:queue-list', 'SoftLayer.CLI.mq.queue_list:cli'),
    ('messaging:queue-pop', 'SoftLayer.CLI.mq.queue_pop:cli'),
    ('messaging:queue-push', 'SoftLayer.CLI.mq.queue_push:cli'),
    ('messaging:queue-remove', 'SoftLayer.CLI.mq.queue_remove:cli'),
    ('messaging:topic-add', 'SoftLayer.CLI.mq.topic_add:cli'),
    ('messaging:topic-detail', 'SoftLayer.CLI.mq.topic_detail:cli'),
    ('messaging:topic-list', 'SoftLayer.CLI.mq.topic_list:cli'),
    ('messaging:topic-push', 'SoftLayer.CLI.mq.topic_push:cli'),
    ('messaging:topic-remove', 'SoftLayer.CLI.mq.topic_remove:cli'),
    ('messaging:topic-subscribe', 'SoftLayer.CLI.mq.topic_subscribe:cli'),
    ('messaging:topic-unsubscribe', 'SoftLayer.CLI.mq.topic_unsubscribe:cli'),

    ('metadata', 'SoftLayer.CLI.metadata:cli'),

    ('nas', 'SoftLayer.CLI.nas'),
    ('nas:list', 'SoftLayer.CLI.nas.list:cli'),
    ('nas:credentials', 'SoftLayer.CLI.nas.credentials:cli'),

    ('object-storage', 'SoftLayer.CLI.object_storage'),
    ('object-storage:accounts',
     'SoftLayer.CLI.object_storage.list_accounts:cli'),
    ('object-storage:endpoints',
     'SoftLayer.CLI.object_storage.list_endpoints:cli'),

    ('order', 'SoftLayer.CLI.order'),
    ('order:category-list', 'SoftLayer.CLI.order.category_list:cli'),
    ('order:item-list', 'SoftLayer.CLI.order.item_list:cli'),
    ('order:package-list', 'SoftLayer.CLI.order.package_list:cli'),
    ('order:place', 'SoftLayer.CLI.order.place:cli'),
    ('order:preset-list', 'SoftLayer.CLI.order.preset_list:cli'),
    ('order:package-locations', 'SoftLayer.CLI.order.package_locations:cli'),
    ('order:place-quote', 'SoftLayer.CLI.order.place_quote:cli'),

    ('rwhois', 'SoftLayer.CLI.rwhois'),
    ('rwhois:edit', 'SoftLayer.CLI.rwhois.edit:cli'),
    ('rwhois:show', 'SoftLayer.CLI.rwhois.show:cli'),

    ('hardware', 'SoftLayer.CLI.hardware'),
    ('hardware:cancel', 'SoftLayer.CLI.hardware.cancel:cli'),
    ('hardware:cancel-reasons', 'SoftLayer.CLI.hardware.cancel_reasons:cli'),
    ('hardware:create', 'SoftLayer.CLI.hardware.create:cli'),
    ('hardware:create-options', 'SoftLayer.CLI.hardware.create_options:cli'),
    ('hardware:detail', 'SoftLayer.CLI.hardware.detail:cli'),
    ('hardware:edit', 'SoftLayer.CLI.hardware.edit:cli'),
    ('hardware:list', 'SoftLayer.CLI.hardware.list:cli'),
    ('hardware:power-cycle', 'SoftLayer.CLI.hardware.power:power_cycle'),
    ('hardware:power-off', 'SoftLayer.CLI.hardware.power:power_off'),
    ('hardware:power-on', 'SoftLayer.CLI.hardware.power:power_on'),
    ('hardware:reboot', 'SoftLayer.CLI.hardware.power:reboot'),
    ('hardware:reload', 'SoftLayer.CLI.hardware.reload:cli'),
    ('hardware:credentials', 'SoftLayer.CLI.hardware.credentials:cli'),
    ('hardware:update-firmware', 'SoftLayer.CLI.hardware.update_firmware:cli'),
    ('hardware:rescue', 'SoftLayer.CLI.hardware.power:rescue'),
    ('hardware:ready', 'SoftLayer.CLI.hardware.ready:cli'),

    ('securitygroup', 'SoftLayer.CLI.securitygroup'),
    ('securitygroup:list', 'SoftLayer.CLI.securitygroup.list:cli'),
    ('securitygroup:detail', 'SoftLayer.CLI.securitygroup.detail:cli'),
    ('securitygroup:create', 'SoftLayer.CLI.securitygroup.create:cli'),
    ('securitygroup:edit', 'SoftLayer.CLI.securitygroup.edit:cli'),
    ('securitygroup:delete', 'SoftLayer.CLI.securitygroup.delete:cli'),
    ('securitygroup:rule-list', 'SoftLayer.CLI.securitygroup.rule:rule_list'),
    ('securitygroup:rule-add', 'SoftLayer.CLI.securitygroup.rule:add'),
    ('securitygroup:rule-edit', 'SoftLayer.CLI.securitygroup.rule:edit'),
    ('securitygroup:rule-remove', 'SoftLayer.CLI.securitygroup.rule:remove'),
    ('securitygroup:interface-list',
     'SoftLayer.CLI.securitygroup.interface:interface_list'),
    ('securitygroup:interface-add',
     'SoftLayer.CLI.securitygroup.interface:add'),
    ('securitygroup:interface-remove',
     'SoftLayer.CLI.securitygroup.interface:remove'),

    ('sshkey', 'SoftLayer.CLI.sshkey'),
    ('sshkey:add', 'SoftLayer.CLI.sshkey.add:cli'),
    ('sshkey:remove', 'SoftLayer.CLI.sshkey.remove:cli'),
    ('sshkey:edit', 'SoftLayer.CLI.sshkey.edit:cli'),
    ('sshkey:list', 'SoftLayer.CLI.sshkey.list:cli'),
    ('sshkey:print', 'SoftLayer.CLI.sshkey.print:cli'),

    ('ssl', 'SoftLayer.CLI.ssl'),
    ('ssl:add', 'SoftLayer.CLI.ssl.add:cli'),
    ('ssl:download', 'SoftLayer.CLI.ssl.download:cli'),
    ('ssl:edit', 'SoftLayer.CLI.ssl.edit:cli'),
    ('ssl:list', 'SoftLayer.CLI.ssl.list:cli'),
    ('ssl:remove', 'SoftLayer.CLI.ssl.remove:cli'),

    ('subnet', 'SoftLayer.CLI.subnet'),
    ('subnet:cancel', 'SoftLayer.CLI.subnet.cancel:cli'),
    ('subnet:create', 'SoftLayer.CLI.subnet.create:cli'),
    ('subnet:detail', 'SoftLayer.CLI.subnet.detail:cli'),
    ('subnet:list', 'SoftLayer.CLI.subnet.list:cli'),
    ('subnet:lookup', 'SoftLayer.CLI.subnet.lookup:cli'),

    ('ticket', 'SoftLayer.CLI.ticket'),
    ('ticket:create', 'SoftLayer.CLI.ticket.create:cli'),
    ('ticket:detail', 'SoftLayer.CLI.ticket.detail:cli'),
    ('ticket:list', 'SoftLayer.CLI.ticket.list:cli'),
    ('ticket:update', 'SoftLayer.CLI.ticket.update:cli'),
    ('ticket:upload', 'SoftLayer.CLI.ticket.upload:cli'),
    ('ticket:subjects', 'SoftLayer.CLI.ticket.subjects:cli'),
    ('ticket:summary', 'SoftLayer.CLI.ticket.summary:cli'),
    ('ticket:attach', 'SoftLayer.CLI.ticket.attach:cli'),
    ('ticket:detach', 'SoftLayer.CLI.ticket.detach:cli'),

    ('user', 'SoftLayer.CLI.user'),
    ('user:list', 'SoftLayer.CLI.user.list:cli'),
    ('user:detail', 'SoftLayer.CLI.user.detail:cli'),
    ('user:permissions', 'SoftLayer.CLI.user.permissions:cli'),
    ('user:edit-permissions', 'SoftLayer.CLI.user.edit_permissions:cli'),
    ('user:edit-details', 'SoftLayer.CLI.user.edit_details:cli'),
    ('user:create', 'SoftLayer.CLI.user.create:cli'),
    ('user:delete', 'SoftLayer.CLI.user.delete:cli'),

    ('vlan', 'SoftLayer.CLI.vlan'),
    ('vlan:detail', 'SoftLayer.CLI.vlan.detail:cli'),
    ('vlan:list', 'SoftLayer.CLI.vlan.list:cli'),

    ('summary', 'SoftLayer.CLI.summary:cli'),

    ('report', 'SoftLayer.CLI.report'),
    ('report:bandwidth', 'SoftLayer.CLI.report.bandwidth:cli'),
]

ALL_ALIASES = {
    'hw': 'hardware',
    'lb': 'loadbal',
    'meta': 'metadata',
    'my': 'metadata',
    'sg': 'securitygroup',
    'server': 'hardware',
    'vm': 'virtual',
    'vs': 'virtual',
    'dh': 'dedicatedhost',
}
