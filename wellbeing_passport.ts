interface WellbeingCredential {
  issuer: "did:web:ssflab.org";
  subject: string;
  credentialSubject: {
    daily_quota_minutes: number;
    quota_used: number;
    contract_hash: string;
    reset: string;
  };
}

export function verifyPassport(jwt: string) {
  const payload = JSON.parse(Buffer.from(jwt.split('.')[1], 'base64').toString());
  const remaining = payload.daily_quota_minutes - payload.quota_used;
  return remaining > 0? {status: 200, remaining} : {status: 429, remaining: 0};
}
