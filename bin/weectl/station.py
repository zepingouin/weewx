#
#    Copyright (c) 2009-2023 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your rights.
#
"""Entry point for the "station" subcommand."""
import sys

import weewx
from . import common_parser
import weecfg.station_config

station_create_usage = """weectl station create [--config=CONFIG-PATH] 
                             [--driver=DRIVER] 
                             [--altitude=ALTITUDE,{foot|meter}]
                             [--latitude=LATITUDE] [--longitude=LONGITUDE]
                             [--register={y,n} [--station-url=STATION_URL]]
                             [--units={us,metricwx,metric}]
                             [--html-root=HTML_ROOT] [--skin-root=SKIN_ROOT]
"""
station_reconfigure_usage = "weectl station reconfigure [--config=CONFIG-PATH] [--driver=DRIVER]"
station_upgrade_usage = "weectl station upgrade [--config=CONFIG-PATH]"
station_upgrade_skins_usage = "weectl station upgrade-skins [--config=CONFIG-PATH]"

station_usage = "\n       ".join((station_create_usage, station_reconfigure_usage,
                                  station_upgrade_usage, station_upgrade_skins_usage))


def add_subparser(subparsers,
                  weewx_root='/home/weewx',
                  html_root='html',
                  skin_root='skins'):
    station_parser = subparsers.add_parser("station",
                                           usage=station_usage,
                                           description="Manages the configuration file and skins",
                                           help="Create, modify, or upgrade a config file")
    action_parser = station_parser.add_subparsers(dest='action',
                                                  title="Which action to take")

    # Action 'create'
    create_station_parser = action_parser.add_parser('create',
                                                     parents=[common_parser],
                                                     usage=station_create_usage,
                                                     help='Create a station config file')
    create_station_parser.add_argument('--driver',
                                       help="Driver to use. E.g., --driver=weewx.drivers.fousb")
    create_station_parser.add_argument('--altitude', metavar="ALTITUDE,(foot|meter)",
                                       help="The station altitude in either feet or meters."
                                            " For example, '750,foot' or '320,meter'")
    create_station_parser.add_argument('--latitude',
                                       help="The station latitude in decimal degrees.")
    create_station_parser.add_argument('--longitude',
                                       help="The station longitude in decimal degrees.")
    create_station_parser.add_argument('--register', choices=['y', 'n'],
                                       help="Register this station in the weewx registry?")
    create_station_parser.add_argument('--station-url',
                                       help="Unique URL to be used if registering the station.")
    create_station_parser.add_argument('--units', choices=['us', 'metricwx', 'metric'],
                                       dest='unit_system',
                                       help="Set display units to us, metricwx, or metric.")
    create_station_parser.add_argument('--html_root',
                                       default='public_html',
                                       help='Set HTML_ROOT, relative to WEEWX_ROOT. '
                                            'Default is "public_html".')
    create_station_parser.add_argument('--skin_root', default='skins')
    create_station_parser.add_argument('--no-prompt', type=bool,
                                       help="If true, suppress prompts")
    create_station_parser.set_defaults(func=create_station)

    # Action 'reconfigure'
    reconfigure_station_parser = action_parser.add_parser('reconfigure',
                                                          parents=[common_parser],
                                                          usage=station_reconfigure_usage,
                                                          help='Reconfigure a station config file')
    reconfigure_station_parser.add_argument('--driver',
                                            help="Set active driver to DRIVER")

    # Action 'upgrade'
    upgrade_station_parser = action_parser.add_parser('upgrade',
                                                      parents=[common_parser],
                                                      usage=station_upgrade_usage,
                                                      help='Upgrade a station config file')

    # Action 'upgrade-skins'
    upgrade_skins_parser = action_parser.add_parser('upgrade-skins',
                                                    parents=[common_parser],
                                                    usage=station_upgrade_skins_usage,
                                                    help='Upgrade the skins')

def create_station(namespace):
    try:
        weecfg.station_config.create_station(config_path=namespace.config,
                                             altitude=namespace.altitude,
                                             latitude=namespace.latitude,
                                             longitude=namespace.longitude,
                                             register=namespace.register,
                                             unit_system=namespace.unit_system,
                                             driver=namespace.driver,
                                             no_prompt=namespace.no_prompt)
    except weewx.ViolatedPrecondition as e:
        sys.exit(e)