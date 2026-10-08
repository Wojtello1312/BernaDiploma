function Para(el)
  local s = pandoc.utils.stringify(el)
  if s:match('^Tabela %d+%.%d+%.') then
    return {pandoc.RawBlock('latex', '\\Needspace{7\\baselineskip}'), el}
  end
end
