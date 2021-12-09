% create signal
srate = 1000;
time = 0:1/srate:3;
n= length(time);
p=15;

% noise level
noisemp=5;
% amplitude modulator and noise level
ampl = interp1(rand(p,1)*30,linspace(1,p,n));
noise = noisemp*randn(size(time));
signal = ampl + noise;

% initialize filtered signal 
filsig = zeros(size(signal));

% implement the running mean filter
k = 20 ;
for i=k+1:n-k-1
    %each point is the average of k surroundings points (point before and point after)
    filsig(i) = mean(signal(i-k:i+k));
end
% compute window size in ms
windowssize = 1000*(k*2+1)/srate; 
% plot the noisy and filtered signal
figure(1) , clf , hold on
plot(time,signal,time,filsig,'linew',2)
xlabel ('time (sec)'),ylabel('Amplitude')
