import Plugin from 'sran.nvim'
import dict from './tran-api'

export default function(plugin: Plugin) {
  const { nvim } = plugin
  const logger = plugin.util.getLogger('dict')
  nvim.on('notification', async (method, args: any[]) => {
    if (method === 'dict_translate') {
      logger.info('args: ', args)
      logger.info('args[0]: ', args[0])
      const result = await dict(args[0], null, null)
      if (result) {
        nvim.command(`echo "${result.word} ${result.phoneticSymbol || ''} ${result.candidate.join(',')}"`)
      }
    }
  })
}
