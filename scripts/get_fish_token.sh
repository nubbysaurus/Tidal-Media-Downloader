B64CREDS=$(echo -n "3dfVgOIjxMSxQQ0A:STpm48VIHSp5JXaZXvCh297bwlatAWuoKfE4kQ026pI=" | base64);
neptune:Tidal-Media-Downloader nubby$ curl -X POST \
> -H "Authorization: Basic $B64CREDS" \
> -d "grant_type=client_credentials" \
> "https://auth.tidal.com/v1/oauth2/token"
